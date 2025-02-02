#!/usr/bin/perl
use strict;
use warnings;
use File::Basename;
use Cwd 'realpath';

my %args;  # Hash to store arguments

my $outdir = 1;
my $command = "";
my $sourcefile = "";

# Process command line arguments
while (@ARGV) {
    my $arg = shift @ARGV;
    if ($arg =~ /^--/) {
        my $key = substr($arg, 2);  # Remove the leading --
        my $value = shift @ARGV;
        if ($key eq "outdir"){
            $outdir = 0;
        } elsif ($key eq "command"){
            $command = $value;
        } elsif ($key eq "sourcefile"){
            $sourcefile = $value;
        }
        push @{$args{$key}}, $value;  # Add the next argument to the array
    }
}

sub bstring{ my $k = $_[0]; $k = "$k"; $k =~ s/'/'"'"'/g; $k =~ s/\t/'"\\t"'/g; $k =~ s/\n/'"\\n"'/g; $k =~ s/\f/'"\\f"'/g; return "'$k'"; }

my @decls=();

while (my ($key, $value) = each %args )
{
   my $value = join(" ", map { bstring($_) } @$value );
   if ($value){
      push @decls, "$key=($value)";
   }
}

if ($outdir){
   push @decls, "outdir='.'";
}

if ($command){
    push @decls, $command;
} elsif ($sourcefile) {
    $sourcefile = bstring($sourcefile);
    push @decls, "source ${sourcefile}";
}

$command = join("\n", @decls);

exit system("bash", "-x", "-c", $command);
