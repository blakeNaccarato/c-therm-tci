---
short_title: "C-Therm TCi Tutorial"
author: "Blake Naccarato"
date: "2024-05-01"
abstract: "A guide to using the C-Therm TCi thermal conductivity instrument in the lab."
exports:
  - format: "pdf"
    output: "tutorial.pdf"
    template: "pdf_template"
---

# C-Therm TCi Tutorial

For more detail, see the manual in the black binder in {numref}`00-01-ref`, the searchable PDF in our lab's Google Drive Shared Drive, or by searching for it online. In this tutorial, we will be testing the thermal conductivity of a Pyrex reference sample. It is always a good idea to start your day's testing with the Pyrex reference sample, so you can compare the measured result with the expected thermal conductivity of 1.143&nbsp;W/m-K. See the reference material standard values in Appendix D on page 118 of the manual.

## Instrument warm-up

First, turn on the instrument by pressing the power button indicated in {numref}`00-04-turn-on`, and the laptop associated with this instrument in {numref}`00-18-laptop`. Note that the language bar in {numref}`00-05-language` may need to be set to "English (United States)" if it is not set already. Open the software by clicking on the icon indicated in {numref}`00-06-desktop-software-indicated`, and you will be prompted with the login dialog in {numref}`00-07-login`. Click "OK" to proceed. The instrument should be left to warm up for about thirty minutes before testing.

Please remember to turn off the instrument and the computer when done testing.

```{figure} _static/tutorial/00-04-turn-on.jpg
:name: 00-04-turn-on
:alt: C-Therm TCi instrument with red box indicating the power button
C-Therm TCi instrument
```
```{figure} _static/tutorial/00-18-laptop.jpg
:name: 00-18-laptop
:alt: Laptop associated with the C-Therm TCi instrument, open and showing the desktop
Laptop for the C-Therm TCi instrument
```
```{figure} _static/tutorial/00-05-language.png
:name: 00-05-language
:alt: Screenshot of the desktop with red box indicating the language selection dialog
Language selection dialog
```
```{figure} _static/tutorial/00-06-desktop-software-indicated.png
:name: 00-06-desktop-software-indicated
:alt: Screenshot of the desktop with red box indicating the software in the toolbar
C-Therm software
```
```{figure} _static/tutorial/00-07-login.png
:name: 00-07-login
:alt: Screenshot of the login screen for the software with red box indicating the "OK" button
Login screen
```

## Protect the sensor

```{warning}
You should always cover the fragile sensor with the protective rubber cap when not in use, as shown in {numref}`00-06-capped`.
```

Also, if you use the ring stand to move the mass between tests, be sure to swing the mass out to the side, as shown in {numref}`00-16-safer`. Do not suspend the mass above the fragile sensor, as shown in {numref}`00-15-damage-will-occur`.

```{figure} _static/tutorial/00-15-damage-will-occur.png
:name: 00-15-damage-will-occur
:alt: Semi-transparent red cross over the image, indicating a bad practice. Mass positioned above the fragile sensor
Don't position the mass above the fragile sensor
```
```{figure} _static/tutorial/00-16-safer.jpg
:name: 00-16-safer
:alt: Better practice of moving the mass to the side of the sensor if needed
Instead, shift the mass to the side when changing samples
```

## Preparing your sample

While waiting for the instrument to warm up, prepare your sample for testing. We will test the Pyrex reference material, which has an expected thermal conductivity of  1.143&nbsp;W/m-K. Locate the manual, reference samples, and quick-reference materials in {numref}`00-01-ref`, to the right of the instrument room entrance. The black binder is the manual, and the quick-reference card in {numref}`00-02-ref` should be inside the binder. The wooden box contains reference samples, and the glove is for handling the samples.

```{figure} _static/tutorial/00-01-ref.jpg
:name: 00-01-ref
:alt: C-Therm manual next to wooden box containing reference samples and glove
C-Therm manual and reference samples
```
```{figure} _static/tutorial/00-02-ref.jpg
:name: 00-02-ref
:alt: TCi Quick Card showing minimum thickness, sample preparation, and contact agent to use for each material type, as well as a general testing procedure.
TCi Quick Card
```

The process for testing a sample is as follows, with the Pyrex reference sample given as an example:

- Remove the cap from the sensor, shown in {numref}`00-06-capped`.
- Apply about four drops of deionized water as the contact agent for polymers, as in {numref}`00-09-four-drops`.
- Place your sample on the sensor as in {numref}`00-10-sample-placed`.
- Place a 500&nbsp;g mass on top of the sample as in {numref}`00-11-weight-placed`. The mass is located in the wooden box in {numref}`00-01-ref`.
- Set up a ring stand and clamp to prevent the mass from falling off the sensor, as shown in {numref}`00-12-ring-stand`. Position the clamp close to, but not touching the mass as in {numref}`00-13-ring-stand-close`.

Now you are ready to follow the process for **Starting a test**. If you are done testing, or changing contact agents, use a lab wipe to dry the sensor with a gloved hand as in {numref}`00-14-wipe`, and replace the cap on the sensor as in {numref}`00-06-capped`.

```{figure} _static/tutorial/00-06-capped.jpg
:name: 00-06-capped
:alt: C-Therm TCi sensor with a protective rubber cap on it
Capped C-Therm TCi sensor
```
```{figure} _static/tutorial/00-09-four-drops.jpg
:name: 00-09-four-drops
:alt: C-Therm TCi sensor with four drops of water on it
Sufficient amount of water on the sensor
```
```{figure} _static/tutorial/00-10-sample-placed.jpg
:name: 00-10-sample-placed
:alt: Pyrex reference sample placed on C-Therm TCi sensor
Pyrex reference sample on sensor
```
```{figure} _static/tutorial/00-11-weight-placed.jpg
:name: 00-11-weight-placed
:alt: C-Therm TCi sensor with Pyrex reference sample on top of it, and a 500 gram mass on top of that
Consistent 500&nbsp;g mass on the sample
```
```{figure} _static/tutorial/00-12-ring-stand.jpg
:name: 00-12-ring-stand
:alt: Ring stand with clamp close to, but not touching, the 500 gram mass, preventing the mass from falling off sideways
Ring stand as guard
```
```{figure} _static/tutorial/00-13-ring-stand-close.jpg
:name: 00-13-ring-stand-close
:alt: Close up of the ring stand with clamp close to but not touching the 500 gram mass
Clamp is close to, but not touching, the mass
```
```{figure} _static/tutorial/00-14-wipe.jpg
:name: 00-14-wipe
:alt: Gloved hand wiping contact agent off of the sensor
Wiping the sensor after testing
```

## Starting a test

Once you have finished **Instrument warm-up** and []**Preparing your sample**, you are ready to begin testing. By making good selections during test setup, such as setting "Material Group", "Material", and "Material Lot" appropriately, it will be easier to process the data after **Exporting results**. After the login process, the main screen will appear. Start a new test by clicking the "New Test" button as shown in {numref}`09-new-test`.

```{tip}
If you are testing a novel sample, make sure to define a unique "Material Lot" to differentiate between it and other tests of the same material. See **Categorizing your samples** for details.
```

Click "Next" after each of the following steps:

- Select your project as in {numref}`10-select-project`, optionally creating one as in {numref}`06-save-project`.
- Select an appropriate test method for the material you intend to test as in {numref}`11-00-select-test-method`. You will usually select "Polymers HR", for example with Pyrex. See **Creating a test method** for more detail.
- Select the Material Group and Material you are testing, as shown in {numref}`11-01-select-material`. For Pyrex, select "Reference Materials", then "Pyrex". You may optionally create one as in {numref}`02-save-material-group` and {numref}`03-add-material`.

On the final screen before the test begins, make the following selections in order as in {numref}`12-select-instrument`:

```{important}
Make sure you follow these steps in order, otherwise you may encounter a bug in the software. See **Something went wrong with setting a "Material Lot" at test time** for more detail.
```

- Select the contact agent you are using, which will usually be water, but could be thermal grease.
- Select or type a new "Material Lot". This "lot" might represent a unique sample identifier, like a date or a number indicating some percent-by-weight of an additive. For instance a lot like "2024-04-30" or "3-cnt" could differentiate your samples from the general "Nafion 117" material.
- Click "Start Test".
- If you are prompted to create a new lot, click "Yes" as in {numref}`13-new-lot-prompt`.

```{tip}
You don't need to select a "Material Lot" for the Pyrex reference sample.
```

Proceed to **checking-on-a-test-run** to monitor the test for the first few measurements, after which you can leave it unattended.

```{figure} _static/tutorial/09-new-test.png
:name: 09-new-test
:alt: Screenshot of software with red box indicating the "New Test" button
"New Test" button on the main screen
```
```{figure} _static/tutorial/10-select-project.png
:name: 10-select-project
:alt: Screenshot of "Select Project" dialog with red box indicating the project to be selected
Select project
```
```{figure} _static/tutorial/11-00-select-test-method.png
:name: 11-00-select-test-method
:alt: Screenshot of "Select Test Method" dialog with red box indicating the test method to be selected
Select test method
```
```{figure} _static/tutorial/11-01-select-material.png
:name: 11-01-select-material
:alt: Screenshot of "Select Material" dialog with red box indicating the material to be selected
Select material
```
```{figure} _static/tutorial/12-select-instrument.png
:name: 12-select-instrument
:alt: Screenshot of "Select Instrument" dialog with sequence of red boxes indicating the process of selecting a contact agent, material lot, and starting the test
Select instrument and start test
```
```{figure} _static/tutorial/13-new-lot-prompt.png
:name: 13-new-lot-prompt
:alt: Screenshot of "New Test" dialog that warns if a chosen lot doesn't exist yet, with red box indicating "Yes" to create it
Create new lot if prompted
```

## Checking on a test run

```{important}
Don't touch the sample from this point onward.
```

After clicking "Start Test", the test will begin. You will want to monitor the first few measurements before leaving the instrument to finish unattended. The initial waiting period is defined as in "Delay before first measurement" in {numref}`08-00-save-test-method` will begin, causing "Wait: Initial" to appear as in {numref}`14-warmup`.

```{figure} _static/tutorial/14-warmup.png
:name: 14-warmup
:alt: Screenshot of the main screen as the test begins
Initial waiting period as test begins
```

The active test indicator will read "reading sample" as in {numref}`15-measuring` when a measurement is being taken. Wait for a few measurements to appear before leaving the machine to finish the test run.

```{figure} _static/tutorial/15-measuring.png
:name: 15-measuring
:alt: Screenshot of the main screen during the test with red box indicating a reading is taking place
Test in progress with reading being taken
```

If the measurements are in-range for the selected test method, the background will be white as in {numref}`16-check-good`. If the measurements are out-of-range, the background will be orange as in {numref}`17-bad-example`. This means that the test method chosen, for instance "Polymers HR", is not appropriate for the material being tested. Our instrument only has calibrations for polymers and foams, and each test method has an acceptable range to which it applies.

You may encounter other issues, such as drifting or inconsistent thermal conductivity measurements. See **Troubleshooting** for details. If you click "Stop Test" and cancel a test before it finishes, you will be prompted with the dialog in {numref}`19-interrupt`. Choose whether to mark the test as valid and continue.

```{figure} _static/tutorial/16-check-good.png
:name: 16-check-good
:alt: Screenshot of test in progress with red box indicating good measurements
Good measurements have a white background
```
```{figure} _static/tutorial/17-bad-example.png
:name: 17-bad-example
:alt: Screenshot of a finished test with red box indicating out-of-range measurements
Example of out-of-range measurements with orange background for a given test method
```
```{figure} _static/tutorial/19-interrupt.png
:name: 19-interrupt
:alt: Screenshot of the interrupted test dialog
Interrupted test dialog
```

A completed and successful test looks like {numref}`18-good-example`, with a white background across all measurements, indicating that they are in range. You still may notice variabliity in repeat tests, or have trouble reproducing the results on different days. See **troubleshooting** for details or review the manual.

```{figure} _static/tutorial/18-good-example.png
:name: 18-good-example
:alt: Screenshot of a completed test with red box indicating good measurements
Example of in-range measurements with white background for a given test method
```

If you ran a test with Pyrex, check that the thermal conductivity values are similar to its expected thermal conductivity of 1.143&nbsp;W/m-K. You may also test the LAF 6720 foam reference sample, choosing the "Foams HR" test method instead. See the reference material standard values in Appendix D on page 118 of the manual.

When you are ready to get your data off of the machine for processing, see **Exporting results**.

## Exporting results

Follow the process below from {numref}`23-export-tests` to {numref}`27-finish-export` to export an XML file of all tests. It is easier to export and process all tests than to just process the latest ones, as the data process includes an Excel file which takes averages of measurements grouped by Project, Material Group, Material, and Lot Number.

```{figure} _static/tutorial/23-export-tests.png
:name: 23-export-tests
:alt: Screenshot of the menu bar with red box indicating the "Test Results" export button
Test results export
```
```{figure} _static/tutorial/24-retrieve-all.png
:name: 24-retrieve-all
:alt: Screenshot of the "Export User Tests" dialog with sequence of red boxes indicating the search and retrieval of all tests
Searching for and retrieving all tests for export
```
```{figure} _static/tutorial/25-select-all.png
:name: 25-select-all
:alt: Screenshot of a now-populated "Export User Tests" dialog with red box indicating the "Select All" button
Selecting all retrieved tests for export
```
```{figure} _static/tutorial/26-select-path.png
:name: 26-select-path
:alt: Screenshot of the "Save As" dialog with redboxes indicating how to export tests as XML to the Desktop
Exporting XML test data to the Desktop
```
```{figure} _static/tutorial/27-finish-export.png
:name: 27-finish-export
:alt: Screenshot of the final "Export User Tests" dialog with red box indicating the "Export" button
Completing the export process
```

## Search for tests

You can search for test results using the "Open Test" dialog. Note that the `*` character functions as a wildcard when searching as in {numref}`28-wildcard-search`.

```{figure} _static/tutorial/28-wildcard-search.png
:name: 28-wildcard-search
:alt: Screenshot of the "Manage Test Methods" dialog with red box indicating an "*" wildcard search example
Example of searching by wildcard using "*"
```

## Categorizing your samples

Test category hierarchy is shown from {numref}`00-08-manage` through {numref}`06-save-project`.

```{figure} _static/tutorial/00-08-manage.png
:name: 00-08-manage
:alt: Screenshot of software with red box indicating the "Manage" button
First screen after logging in
```
```{figure} _static/tutorial/00-09-manage-dialog-important-options.png
:name: 00-09-manage-dialog-important-options
:alt: Screenshot of the "Manage" dialog with red box indicating "Material Group", "Material", "Material Lot", "Project", and "Test Method" buttons
"Manage" dialog
```
```{figure} _static/tutorial/01-add-material-group.png
:name: 01-add-material-group
:alt: Screenshot of the "Manage Material Groups" dialog with red box indicating the "Add" button
Adding a material group
```
```{figure} _static/tutorial/02-save-material-group.png
:name: 02-save-material-group
:alt: Screenshot of the "Add Material Group" dialog with red box indicating the "Save" button
Saving a material group
```
```{figure} _static/tutorial/03-add-material.png
:name: 03-add-material
:alt: Screenshot of the "Edit Material" dialog with red box indicating the "Save" button
Adding or editing a material
```
```{figure} _static/tutorial/05-save-lot.png
:name: 05-save-lot
:alt: Screenshot of the "Edit Material Lot" dialog with red box indicating the "Save" button
Adding or editing a material lot
```
```{figure} _static/tutorial/06-save-project.png
:name: 06-save-project
:alt: Screenshot of the "ADd Project" dialog with red box indicating the "Save" button
Adding or editing a project
```

## Creating a test method

Test methods can be created or edited as in {numref}`07-test-method` and {numref}`08-00-save-test-method`.

```{figure} _static/tutorial/07-test-method.png
:name: 07-test-method
:alt: Screenshot of the "Manage Test Methods" dialog with red box indicating the material method to be edited
Example of editing the "Polymers HR (16 measurements)" test method
```
```{figure} _static/tutorial/08-00-save-test-method.png
:name: 08-00-save-test-method
:alt: Screenshot of the "Edit Test Method" dialog with red boxes indicating the "Save" button, the "Get Ambient Temperature for each Measurement" checkbox, and the most important fields like "Delay", "Min Measurement Period", and "Number of Measurements"
Adding or editing a test method
```

## Alternative category navigation

Sample categories connect to one another, allowing you to browse the Materials belonging to a Material Group, the Lots for each Material, and so-on. See this kind of navigation in {numref}`08-01-relationships-1` and {numref}`08-02-relationships-2`.

```{figure} _static/tutorial/08-01-relationships-1.png
:name: 08-01-relationships-1
:alt: Screenshot of various dialogs with a sequence of red boxes indicating relationships between "ExampleGroup", "ExampleMaterial1", and "ExampleMaterial2"
Relationships between "ExampleGroup", "ExampleMaterial1", and "ExampleMaterial2"
```
```{figure} _static/tutorial/08-02-relationships-2.png
:name: 08-02-relationships-2
:alt: Screenshot of various dialogs with a sequence of red boxes indicating relationship between "ExampleMaterial1" and "Lot 1"
Relationship between "ExampleMaterial1" and "Lot 1"
```

## Troubleshooting

Here are a few issues encountered by our group, but the troubleshooting guide in section 8.4.2 on page 89 of the manual is more thorough. Find the manual in the black binder in {numref}`00-01-ref` or in the searchable PDF in our lab's Google Drive Shared Drive.

### Something went wrong with setting a "Material Lot" at test time

The software has a bug where if you don't select "Contact Agent" **before** entering a new "Material Lot", the test will try to start without properly creating the new lot. Make sure you select "Contact Agent" first, then create the new lot.

### Thermal conductivity steadily decreases during a test

Your material may be hygroscopic, meaning it absorbs water, and is absorbing the deionized water used as a contact agent, resulting in varying test conditions and a gradually decreasing thermal conductivity reading over time. Or you may be taking readings over an especially long interval, and the water is evaporating. You may use OMEGATHERM 201 thermal paste as an alterative contact agent if you are testing a hygroscopic material or taking measurements over a long time interval

### Thermal conductivity readings inconsistent during tests or between tests

Your sample may be too thin. See section 4.6 on page 33 of the manual, in the black binder in {numref}`00-01-ref` or in the searchable PDF in our lab's Google Drive Shared Drive.

```{figure} _static/tutorial/00-17-blotter.jpg
:name: 00-17-blotter
:width: 50%
:alt: LAF 6720 foam reference sample placed on top of the Pyrex sample
Using the LAF 6720 foam reference sample for a blotter test
```

### Overlaying individual measurements

It is sometimes helpful to overlay the voltage-over-time curves of individual measurements when troubleshooting measurement inconsistencies. You can do this by right-clicking on a selection of measurements and selecting "Overlay Voltage Chart" as in {numref}`20-overlay`. This will show the voltage data chart as in {numref}`21-overlay-chart`. For a good test, the curves should all appear similar, and with similar inflection. The latter fifth of the chart is linearized and used to determine thermal properties, so if inflection varies there, the resulting thermal conductivity will be different.

```{figure} _static/tutorial/20-overlay.png
:name: 20-overlay
:alt: Screenshot of a test result with red box indicating the "Overlay Voltage Chart" context menu item
Overlaying a voltage chart of multiple measurements
```
```{figure} _static/tutorial/21-overlay-chart.png
:name: 21-overlay-chart
:alt: Screenshot of "Voltage Data Chart"
Voltage data chart
```

### Test results aren't updating

The test results filter pane must be "reset" when new tests are taken as in {numref}`22-tests`. This re-populates the list of tests in the main window for browsing. This is only needed if you wish to browse the tests there, otherwise you can find and filter tests from the "Open Test" dialog.

```{figure} _static/tutorial/22-tests.png
:name: 22-tests
:alt: Screenshot of "Test Results Filter" pane with red box indicating the "Reset" button
Resetting the test results filter
```
