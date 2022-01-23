#!/usr/bin/env python3

import iterm2
import AppKit
import sys
import json

# Launch the app if its not already open
bundle = "com.googlecode.iterm2"
if not AppKit.NSRunningApplication.runningApplicationsWithBundleIdentifier_(bundle):
    AppKit.NSWorkspace.sharedWorkspace().launchApplication_("iTerm")


async def main(connection):

    # Get the list of avaliable windows arrangements
    arrangements = await iterm2.Arrangement.async_list(connection)

    # Format a json for script filter
    # https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
    formatted_results = []

    if len(arrangements) == 0:
        result = {
            "title": "No arrangements found.",
            "subtitle": "Please make sure you have at least one window arrangement avaliable on iterm.",
        }
        formatted_results.append(result)
    else:
        for arrangement in arrangements:
            result = {
                "title": arrangement,
                "subtitle": "Restore the " + arrangement + " arrangement",
                "arg": arrangement,
                "autocomplete": arrangement,
                "icon": {
                    "path": "./icon.png"
                }
            }
            formatted_results.append(result)

    # Return the avaliable arrangements on alfred joson format
    alfred_json = json.dumps({"items": formatted_results}, indent=2)
    sys.stdout.write(alfred_json)

# Passing True for the second parameter means keep trying to
# connect until the app launches.
iterm2.run_until_complete(main, True)
