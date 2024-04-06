# We are going to look at input and output in Python. Input/Output, I/O, just means getting data into a program,
# and getting it out again.

# It's rare that you need to worry about the file pointer - you can treat a text file like a list.
# We'll have a look at 'binary' data files later in the section, and see how we can choose which values to read.

# We'll also see various ways to write data to a file.

# Files are stored in directories.
# Directory is just a container for files. In fact, directories are also called folders.

# The root directory (or folder) is the top level directory on a drive (in Windows). Each drive has its own root
# directory.

# Linux and Mac (descended from UNIX) don't use drive letters like Windows does (C, D etc.). That means there's only
# one root directory for the whole file system. On those OSs, the root directory is represented by a slash /.

# An 'absolute path' will get you to your destination, no matter where you start from.

# A 'relative path' will get you there from where you are now. If you use it from somewhere else, you won't get where
# you want to be.

# When working with relative paths, there are two useful shortcuts you can use (Linux/Mac):
# You use dot slash, to tell the OS to execute a file in the current directory.
# dot dot - two periods - refers to the directory above the current one.

# On Windows, filenames aren't case-sensitive.
# On Linux, file names are always case-sensitive.
# On Mac OS, by default, file names are not case-sensitive. But they are case-preserving. You can't create them in the
# same directory, because the names would clash. If you attempted to, you'd end up with just the contents of the last
# one, but preserving the case of the first filename.

# As a guide, treat all filenames as case-sensitive.
