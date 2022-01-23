#!/usr/local/bin/python3

import iterm2
import sys
import AppKit

# Launch the app if its not already open
bundle = "com.googlecode.iterm2"
if not AppKit.NSRunningApplication.runningApplicationsWithBundleIdentifier_(bundle):
    AppKit.NSWorkspace.sharedWorkspace().launchApplication_("iTerm")


async def main(connection):
    app = await iterm2.async_get_app(connection)

    # Foreground the app
    await app.async_activate()

    # Restore the selected window arrangement
    await iterm2.Arrangement.async_restore(connection, sys.argv[1])

# Passing True for the second parameter means keep trying to
# connect until the app launches.
iterm2.run_until_complete(main, True)
