## Self Discharge Analyzer

BT2152A, BT2152B

![Image](%20BT2152B-prg_artifacts/image_000000_4fb72be2df6bbfe9247a50bbf2aa72570bac29d36ca7110868bba264d6de02c0.png)

KEYSIGHT

| Legal and Safety Information                                          |   6 |
|-----------------------------------------------------------------------|-----|
| Legal Notices                                                         |   6 |
| Safety Symbols                                                        |   8 |
| Safety Notices                                                        |   9 |
| 1 Quick Reference                                                     |  11 |
| Welcome                                                               |  12 |
| What is Self-discharge?                                               |  12 |
| Advantages of the Keysight BT2152A/B Self-Discharge Analyzer          |  12 |
| Contact Keysight Technologies                                         |  12 |
| Modelsand Specifications                                              |  13 |
| Models                                                                |  13 |
| Front and Rear Views                                                  |  13 |
| Specifications                                                        |  15 |
| Characteristics                                                       |  15 |
| External Temperature Measurement                                      |  17 |
| Dimensions and Weight                                                 |  17 |
| CommandQuick Reference                                                |  18 |
| 2 Installing the Analyzer                                             |  23 |
| Before Installation                                                   |  24 |
| Inspect the Unit                                                      |  24 |
| Check for Items Supplied                                              |  24 |
| Accessories                                                           |  24 |
| Review Safety Information                                             |  25 |
| Observe Environmental Conditions                                      |  25 |
| Provide Adequate Air Flow                                             |  25 |
| Connect the Power Cord                                                |  26 |
| Connect the Interfaces                                                |  27 |
| LAN Connections                                                       |  27 |
| USBConnections                                                        |  28 |
| Digital Port Connections                                              |  28 |
| Thermistor Connections                                                |  28 |
| Connect the Cell Cables                                               |  29 |
| To Keysight Model BT2152A                                             |  29 |
| To Keysight Model BT2152B                                             |  32 |
| 3 Operating the Analyzer                                              |  35 |
| Understanding Front Panel Operation                                   |  36 |
| What happens at power-on?                                             |  36 |
| What happenswhen a test is initiated?                                 |  37 |
| What happenswhen a test stops?                                        |  37 |
| What happenswhen the reference temperature exceeds its specification? |  37 |
| What happenswhen a protection event, inhibit, or error occurs?        |  37 |
| Understanding the Digital Port                                        |  38 |
| Digital Control Port                                                  |  38 |
| Bi-Directional Digital I/O                                            |  38 |
| Digital Input                                                         |  39 |
| Fault Output                                                          |  40 |

| Inhibit Input                                                                            | 40      |
|------------------------------------------------------------------------------------------|---------|
| Synchronized Triggering for Calibrating Wire Resistance and Initiating Tests across Mul- |         |
| tiple BT2162B Instruments                                                                | 41      |
| Fault/ Inhibit System Protection                                                         | 47      |
| Using the WebInterface Cell Testing Tipsand Best Practices                               | 48 51   |
|                                                                                          | 51      |
| ACell's Percent State of Charge                                                          |         |
| Charge Redistribution and Equilibrium                                                    | 51      |
| Expected Self-Discharge Current and Temperature Dependency                               | 52      |
| Temperature Impact on Current Measurement                                                | 52      |
| Impact of Stress and Vibration on Current Measurement                                    | 53      |
| Noise Removal Functions                                                                  | 53      |
| Optimizing the Initial Current and Resistance Settings                                   | 54      |
| Programming Reference                                                                    | 57      |
| Introduction to the SCPI Language                                                        | 58      |
| Command Types                                                                            | 58      |
| Keywords                                                                                 | 58      |
| Queries                                                                                  | 59      |
| Syntax Conventions                                                                       | 59      |
| Parameter Types                                                                          | 59      |
| Device Clear                                                                             | 61      |
| Programming Samples                                                                      | 62      |
| Setting up and running a test                                                            | 62      |
| Retrieving all test values                                                               | 63      |
| Stopping/aborting a test                                                                 | 64      |
| Clearing protection events and errors                                                    | 64      |
| CommandsbySubsystem                                                                      | 65      |
| Calibration Commands Common Commands                                                     | 66      |
| CONFigureCommand                                                                         | 72      |
|                                                                                          | 76      |
| Digital Commands                                                                         | 77      |
| Fetch Commands                                                                           | 79      |
| Format Command                                                                           | 86      |
| InitiateCommands                                                                         | 87      |
| LXI Command                                                                              | 89      |
| Output Commands                                                                          | 90      |
| SenseCommands                                                                            | 91      |
| StatusCommands                                                                           | 93      |
| System Commands                                                                          | 97      |
| StatusTutorial                                                                           | 105     |
| Status Registers                                                                         | 105     |
| Alarm Channel Groups                                                                     | 105     |
| Alarm Status Group                                                                       | 106     |
| Standard Operation Group                                                                 | 106     |
| Status Byte Register Error and Output Queues                                             | 107 108 |
| Status Diagram                                                                           |         |
|                                                                                          | 109     |

| Reset and Interface Settings               |   110 |
|--------------------------------------------|-------|
| SCPI Error Messages                        |   111 |
| Error List                                 |   111 |
| Verification and Calibration               |   117 |
| Verification Procedure                     |   118 |
| Introduction                               |   118 |
| Verification Fixtures                      |   118 |
| Zero-Scale Current Accuracy Verification   |   119 |
| Full-Scale Current Accuracy Verification   |   120 |
| Voltage Accuracy Verification              |   121 |
| Reference Calibration                      |   123 |
| Introduction                               |   123 |
| External DMMConnections and Setup          |   123 |
| Enter Calibration Mode                     |   124 |
| Voltage Calibration                        |   124 |
| Current Calibration                        |   124 |
| End Calibration and Store Results          |   125 |
| Channel Calibration                        |   126 |
| Prerequisites                              |   126 |
| Running Channel Calibration                |   126 |
| If Problems Occur with Channel Calibration |   126 |
| Aborting Channel Calibration               |   126 |
| Wire Resistance Calibration                |   127 |
| Benefits of Wire Resistance Calibration    |   127 |
| In situ Calibration Procedure              |   127 |
| By-short Calibration Procedure             |   128 |
| Calibration Security Reset                 |   129 |
| Electrostatic Discharge (ESD) Precautions  |   129 |
| Tools Required                             |   129 |
| Cover Removal                              |   129 |
| Password Reset                             |   130 |
| Maintenance                                |   131 |
| Index                                      |   132 |

## Legal and Safety Information

Legal Notices

Safety Notices

Safety Symbols

Legal Notices

## Copyright Notice

© Copyright Keysight Technologies 2017- 2020, 2023, 2025

No part of this manual may be reproduced in any form or by any means (including electronic storage and retrieval or translation into a foreign language) without prior agreement and written consent from Keysight Technologies Inc. as governed by United States and international copyright laws.

## Manual Part Number

BT2152A-90001

## Edition

Edition 6, March, 2025

## Published By

Keysight Technologies 900 S. Taft Ave. Loveland, CO80537 USA

## Warranty

The material contained in this document is provided "as is," and is subject to being changed, without notice, in future editions. Further, to the maximum extent permitted by applicable law, Keysight disclaims all warranties, either express or implied, with regard to this manual and any information contained herein, including but not limited to the implied warranties of merchantability and fitness for a particular purpose. Keysight shall not be liable for errors or for incidental or consequential damages in connection with the furnishing, use, or performance of this document or of any information contained herein. Should Keysight and the user have a separate written agreement with warranty terms covering the material in this document that conflict with these terms, the warranty terms in the separate agreement shall control.

## Certification

Keysight Technologies certifies that this product met its published specifications at time of shipment from the factory. Keysight Technologies further certifies that its calibration measurements are traceable to the United States National Institute of Standards and Technology, to the extent allowed by the Institute's calibration facility, and to the calibration facilities of other International Standards Organization members.

## U.S. Government Rights

The Software is "commercial computer software," as defined by Federal Acquisition Regulation ('FAR') 2.101. Pursuant to FAR12.212 and 27.405-3 and Department of Defense FARSupplement ('DFARS') 227.7202, the U.S. government acquires commercial computer software under the same terms by which the software is customarily provided to the public. Accordingly, Keysight provides the Software to U.S. government customers under its standard commercial license, which is embodied in its End User License Agreement (EULA), a copy of which can be found at http://www.keysight.com/find/sweula. The license set forth in the EULA represents the exclusive authority by which the U.S. government may use, modify, distribute, or disclose the Software. The EULA and the license set forth therein, does not require or permit, among other things, that Keysight: (1) Furnish technical information related to commercial computer software or commercial computer software documentation that is not customarily provided to the public; or (2) Relinquish to, or otherwise provide, the government rights in excess of these rights customarily provided to the public to use, modify, reproduce, release, perform, display, or disclose commercial computer software or commercial computer software documentation. No additional government requirements beyond those set forth in the EULA shall apply, except to the extent that those terms, rights, or licenses are explicitly required from all providers of commercial computer software pursuant to the FARand the DFARSand are set forth specifically in writing elsewhere in the EULA. Keysight shall be under no obligation to update, revise or otherwise modify the Software. With respect to any technical data as defined by FAR2.101, pursuant to FAR12.211 and 27.404.2 and DFARS 227.7102, the U.S. government acquires no greater than Limited Rights as defined in FAR27.401 or DFAR227.7103-5 (c), as applicable in any technical data

## Declaration of Conformity

Declarations of Conformity for this product and for other Keysight products may be downloaded from the Web. Go to http:/ / www.keysight.com/ go/ conformity and click on "Declarations of Conformity". You can then search by product number to find the latest Declaration of Conformity.

## Waste Electrical and Electronic Equipment (WEEE) Directive 2002/ 96/ EC

This product complies with the WEEEDirective 2002/96/ECmarketing requirement. The affixed product label (see below) indicates that you must not discard this electrical/ electronic product in domestic household waste.

Product Category: With reference to the equipment types in the WEEEdirective Annex 1, this product is classified as "Monitoring and Control instrumentation" product.

Do not dispose in domestic household waste.

To return unwanted products, contact our local Keysight office.

![Image](%20BT2152B-prg_artifacts/image_000001_4c6c79e0f93125806a2191eee57390508de54d6087378faec9993a2b4a3d86ea.png)

X

## Safety Symbols

![Image](%20BT2152B-prg_artifacts/image_000002_01dbf68dd3275d1925f2ba7ef22ed16f3006679a530a0183496ef32ea312e07c.png)

AWARNINGnoticedenotesahazard. It callsattention toan operating procedure, practice, or the like that, if not correctly performed or adhered to, could result in personal injury or DEATH. Do not proceed beyond a WARNINGnotice until the indicated conditionsare fullyunderstood and met.

CAUTION

![Image](%20BT2152B-prg_artifacts/image_000003_3b0def3105295df7e7fbfc3cc8f81cdfca4e382136cb4ea4769146f74bc11217.png)

![Image](%20BT2152B-prg_artifacts/image_000004_2cbbd904852390e33a061ce86cbde8585a2c2dba89394429d9ed99b2a9abbb38.png)

![Image](%20BT2152B-prg_artifacts/image_000005_7711adcd182aa5f4e201619d91df21ae1fafb3583e22c25daaddaf162b10cf8d.png)

![Image](%20BT2152B-prg_artifacts/image_000006_d56cf91a2253e0e3fbd304808bf5e4440c2469d4c0753b0c272e571802dabd87.png)

![Image](%20BT2152B-prg_artifacts/image_000007_e3a8a94e518e89501e321b94e06095ceabe89a51fc265c70ccfa80380bb16049.png)

![Image](%20BT2152B-prg_artifacts/image_000008_ef390d9d5f9c04b9be94cac13a65566e5980c2cc5a6d3065e4ccd6e4a32784f7.png)

![Image](%20BT2152B-prg_artifacts/image_000009_cb4032996e198426aa8c2d09e34d7a2fb7c6350d72195f828b19935bcd69a7dc.png)

![Image](%20BT2152B-prg_artifacts/image_000010_36c36e7645e85261a768f6d8fb0a8526371f0553f1955bbdee9cb3e059ed6655.png)

![Image](%20BT2152B-prg_artifacts/image_000011_d3bb4b02752fba5893998dd16b2f76e3942ffade04f7a6fc519fbfc3d6e89669.png)

Intertek

![Image](%20BT2152B-prg_artifacts/image_000012_8cf6bdb079afdc2cf3016af406e18c68ee77ca3e5d812a783483a542680814a4.png)

![Image](%20BT2152B-prg_artifacts/image_000013_5b9f591ac0920a239da214ae42161ec2342b997464f34a9c18db4d4b423613b4.png)

KC

![Image](%20BT2152B-prg_artifacts/image_000014_52f4a336ebef129cff501b75574d4bff00440d0069d132ed42be78f7419f5417.png)

ISM1-A

ICES/NMB001

ACAUTION notice denotes a hazard. It calls attention to an operating procedure, practice, or the like that, if not correctly performed or adhered to, could result in damage to the product or loss of important data. Do not proceed beyond a CAUTION notice until the indicated conditions are fully understood and met.

Direct current

Alternating current

Frame or chassis terminal

Standby supply. The unit is not completely disconnected from AC mains when the power switch is off.

CAUTION

Risk of electric shock.

The user must read the instructions before operating to avoid incorrect use - potentially leading to a hazard. CAUTION

Earth ground terminal

The CEmark is a registered trademark of the European Community.

The ETL mark is a registered trademark of Intertek.

The RCM mark is a registered trademark of the Spectrum Management Agency of Australia. This signifies compliance with the Australian EMC Framework regulations under the terms of the Radio Communications Act of 1992.

South Korean Class A EMCDeclaration

This equipment is Class A suitable for professional use and is for use in electromagnetic environments outside of the home.

Contains one or more of the 6 hazardous substances above the maximum concentration value (MCV), 40 Year EPUP.

This text indicates that the instrument is an Industrial Scientific and Medical Group 1 Class A product (CISPER11, Clause 4).

This text indicates product compliance with the Canadian Interference- Causing Equipment Standard (ICES-001).

## Safety Notices

The following general safety precautions must be observed during all phases of operation of this instrument. Failure to comply with these precautions or with specific warnings or instructions elsewhere in this manual violates safety standards of design, manufacture, and intended use of the instrument. Keysight Technologies assumes no liability of the customer's failure to comply with the requirements.

## General WARNING

Donot use thisproduct in anymanner not specified bythe manufacturer. The protective featuresof thisproduct maybe impaired if it isused in a manner not specified in the operating instructions.

## WARNING

Environmental Conditions

Never use the instrument outside of the specified environmental conditionsdescribed under Environmental Conditions.

## Groundthe Instrument WARNING

Thisproduct isprovided with protective earth terminals. To minimize shock hazard, the instrument must be connected to the AC mainsthrough a grounded power cable, with the ground wire firmlyconnected to an electrical ground (safetyground) at the power outlet. Anyinterruption of the protective (grounding) conductor or disconnection of the protective earth terminal will cause a potential shock hazard that could result in injuryor death.

## WARNING

## WARNING

## WARNING

## WARNING

DoNot Operate in an Explosive Atmosphere Donot operate the instrument in the presence of flammable gasesor fumes.

DoNot RemovetheInstrument Cover

Onlyqualified, service-trained personnel who are aware of the hazardsinvolved should remove covers. Alwaysdisconnect external power before servicing.

DoNot Modifythe Instrument

Donot install substitute partsor perform anyunauthorized modification to the product. Returnthe product to a Keysight Salesand Service Office for service and repair to ensure that safetyfeaturesare maintained.

Fuses

The instrument containsan internal fuse, which isnot customer accessible.

## Legal and Safety Information

WARNING

WARNING

Cleaning

Toprevent electric shock, alwaysunplug the unit before cleaning. Use a drycloth or one slightly dampened with water to clean the external case parts. Do not use detergent or chemical solvents. Do not attempt to clean internally.

In Case of Damage

Instrumentsthat are not functioning correctly, appear damaged or defective should be madeinoperative and secured against unintended operation until theycan be repaired byqualified service personnel.

![Image](%20BT2152B-prg_artifacts/image_000015_12a22d464d9a3558f59286fac10e7d1323b96785c70a9c4f1883ebb1dddfbf12.png)

## 1 Quick Reference

Welcome

Modelsand Specifications

CommandQuick Reference

## Welcome

## What isSelf-discharge?

Self-discharge of an electrical cell is the loss of charge over time while not connected to any load. Someamount of self-discharge is a normal attribute resulting from chemical reactions taking place within the cell. Additional self-discharge can result from leakage current paths existing within the cell. Particulate contaminants and dendrite growths produce internal 'micro-shorts', creating such leakage current paths. These are not normal attributes and they can lead to catastrophic failure of the cell. For this reason it is a priority to evaluate cells for self-discharge.

Electrically, self-discharge can be modeled as a high-value resistance existing in parallel across the cell. Note that self-discharge current is very difficult to measure in practice. Usually a defective cell can only be detected after days or weeks of aging. This is where the proprietary technology of the Keysight BT2152A/B Self-Discharge Analyzer provides a superior method of self-discharge measurement (SDM) over other traditional methods.

## Advantagesof the Keysight BT2152A/BSelf-Discharge Analyzer

The Keysight BT2152A/B Self-Discharge Analyzer uses a proprietary measurement technique to determine the open-circuit discharge of the cell due to its internal parallel resistance. This proprietary direct measurement technique lets you determine the quality of the cell within one to two hours after the cell has been initially charged and rested. This can significantly reduce the test time required to determine the self-discharge characteristic of the cell due to internal parallel resistance. Key test features are as follows:

- l The voltage applied to the cell is quickly matched (±5 μ V) to the actual cell voltage. This minimizes any new charge or discharge and limits any new RC settling to a minimum.
- l The voltage applied to the cell is very stable (±10 μ V peak ) to minimize continuing charge redistribution current noise on the self-discharge measurement (SDM).
- l For Keysight Model BT2152A, the measurement system accurately measures low-level self-discharge currents to ± (0.33% of reading + 1 μ A).
- l For Keysight Model BT2152B, the measurement system accurately measures low-level self-discharge currents to ± (0.3% of reading + 0.25 μ A).

## Contact Keysight Technologies

Click www.keysight.com/find/assist to contact Keysight for warranty, service, or technical support. Alternatively you can contact your Keysight Technologies representative.

If you find a Keysight product or solution is impacted by a cyber security issue, please report it using this link: Report a Product Cyber Security issue | Keysight.

For more information about Li-Ion cell self-discharge and Keysight's self-discharge measurement solution, refer to www.keysight.com/ find/ self-discharge.

## Modelsand Specifications

Front and Rear Views

Specifications

Characteristics

External Temperature Measurement

Dimensionsand Weight

## Models

- l Keysight BT2152A- 32 channel Self-Discharge Analyzer
- l Keysight BT2152B - 32 channel Self-Discharge Analyzer

## Front and Rear Views

![Image](%20BT2152B-prg_artifacts/image_000016_cd84a57a8319d7ad393aee2229b854b7a08b00c6c6c0d167b3141b8cee7e359c.png)

## 1. Line switch

Turns the unit on or off

2. StatusIndicators andswitches

3. Air Inlet Power : Green indicates power is on.

LAN : Green indicates the LAN connection is active. Flashing green indicates an LXI identification query is sent. Flashing blue indicates a SCPI command is received. Red indicates a LAN fault.

Ready : Amber indicates the unit is warming up. A warmup time of 1 hour is required. Green indicates the unit is ready to start the test.

Test : Flashing blue indicates that cell matching has been initiated. Blue indicates a test is running. Off indicates no test is running. Flashing orange indicates calibration.

Error : Red indicates an error has occurred. Off indicates protection is cleared.

LAN reset : This recessed switch performs a software system LAN reset.

Aux : This switch is reserved for future use.

Stop : This button aborts any current measurements and sequences. Must be held for 1 second. The unit returns to a state of being ready for initialization.

Air inlet requires a minimum of 6 inch (15 cm) clearance

## 1 Quick Reference

![Image](%20BT2152B-prg_artifacts/image_000017_088bdb7f7481ef6fff29dce7732f9377b0d3f387da5852393c2383030b97991c.png)

## [NOTE](note.gif)

Optional configurations are available in 4- channel increments. The number of available channels are determined by the option number. For example, Option 004 enables channels 1-4 starting from the left; Option 008 enables channels 1-8; Option 016 enables channels 1-16, and Option 032 enables all 32 channels. See SYST:LIC:CAT?

| 4. Fan/Air Outlet                                           | The rear air outlet requiresaminimum of 6 inch (15 cm) clearance.                                                                                                                    |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5. Connectors TheKeysight BT2152Ahaseight RJ45connectorsfor | for channels1-16 channels1- 16.Four cell connectionsareavailableon eachRJ45connector.Seepreviousnote.                                                                                |
|                                                             | TheKeysight BT2152BhasaDB-37connector for channels1-16.Seepreviousnote.                                                                                                              |
| 6. Temperature sensor                                       | Temperature sensor input (requiresan external 10 k Ω thermistor).                                                                                                                    |
| 7. Connectors                                               | for channels17-32 TheKeysight BT2152Ahaseight RJ45connectorsfor channels17- 32.Four cell connectionsareavailable oneachRJ45connector.Seepreviousnote.                                |
|                                                             | TheKeysight BT2152BhasaDB-37connector for channels17-32.Seepreviousnote.                                                                                                             |
| 8. Calibration port The calibration port.                   |                                                                                                                                                                                      |
| 9. Digital connector                                        | An 8-pin digital IOinterface.                                                                                                                                                        |
| 10.USB USBinterface connector.                              |                                                                                                                                                                                      |
| 11. ACinput                                                 | Astandard IEC320 connector.                                                                                                                                                          |
| 12. LAN                                                     | 10/100/1000 Base-TLAN connection. The left LEDindicates link speed: green is1 Gbps, orange is100 Mbps, off is10 Mbps(with activity blinking). The right LEDindicates link integrity. |

## Specifications

Unless otherwise noted, specifications are warranted over the ambient temperature range of 20°Cto 30°Cafter a 1 hour warm-up period. Specifications apply at the connector terminals.

| Parameter                       | BT2152A Specifications      | BT2152B Specifications      |
|---------------------------------|-----------------------------|-----------------------------|
| Number of channels:             | 4to32in4-channel increments | 4to32in4-channel increments |
| Voltagerange:                   | 0.5Vto+4.5V                 | 0.5Vto+4.5V                 |
| Current measurement range:      | ±10mA                       | ±10mA                       |
| Current measurement accuracy: 1 | ±(0.33%of reading+1 μ A)    | ±(0.3%+0.25 μ A)            |
| Voltagemeasurement accuracy: 1  | ±(0.05%of reading+1mV)      | ±(0.04%+0.10mV)             |

## Characteristics

Characteristics are not warranted but are descriptions of performance determined either by design or by type testing. Characteristics are typical unless otherwise noted.

| Parameter                                  | BT2152A Characteristic                                                                                                                                                                                                                                                                                | BT2152B Characteristic                                                                                                                                                                                                                                                                                |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Voltagesourcingstability:                  | ±10 μ Vpeak;±5 μ Vpeaktypical 1                                                                                                                                                                                                                                                                       | ±3 μ Vpeak;±0.85 μ Vpeaktypical 1,2                                                                                                                                                                                                                                                                   |
| Initia l cell voltagematchingaccuracy:     | ±5 μ Vtypical                                                                                                                                                                                                                                                                                         | ±1.25 μ Vtypical                                                                                                                                                                                                                                                                                      |
| Initia l cell current programmingaccuracy: | ±(0.33%+1 μ A)typical                                                                                                                                                                                                                                                                                 | ±(0.3%+0.25 μ A)typical                                                                                                                                                                                                                                                                               |
| Programmableresistancerange:               | 0.1 Ω to10 Ω                                                                                                                                                                                                                                                                                          | 0.05 Ω to10 Ω                                                                                                                                                                                                                                                                                         |
| Programmableresistanceaccuracy: 3          | ±(100m Ω +1.5m Ω / Ω of wiringresistance) resistance . Thisisnot includedintheby-short                                                                                                                                                                                                                | ± (25m Ω +1.5m Ω / Ω of wiringresistance) calibrationmethod.                                                                                                                                                                                                                                          |
|                                            |  Appliestoby-short,insituHIG Hcurrent,andinsituME DIUMcurrent.For insituLOW current,add±5m Ω .  By-short methodhasadditional error term(not included)dueto changesincontact resistance whenreplacingshortswithcells.  Insitucalibrationmethodprovidesresultsthat includethecell'sequivalent series |  Appliestoby-short,insituHIG Hcurrent,andinsituME DIUMcurrent.For insituLOW current,add±5m Ω .  By-short methodhasadditional error term(not included)dueto changesincontact resistance whenreplacingshortswithcells.  Insitucalibrationmethodprovidesresultsthat includethecell'sequivalent series |

## 1 Quick Reference

| Parameter                                                                               | Common Characteristics                                                                                                                                                        |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Voltage/current measurement interva l:                                                  | 1.0secondsto256secondsin1- secondincrements                                                                                                                                   |
| Maximumnumber of readings:                                                              | 259200per channel (onereading=1current measurement +1voltage measurement)                                                                                                     |
| Minimumsupportedcell effectivecapacitance:                                              | 100Farads                                                                                                                                                                     |
| Maximumtest duration:                                                                   | 72hoursat 1-secondmeasurement interva l                                                                                                                                       |
| (=measurement interva l * maximumnumber of                                              | 750daysat 250-secondmeasurement interva l                                                                                                                                     |
| readings)                                                                               | 50seconds                                                                                                                                                                     |
| Minimumsupportedproduct of cell effective capacitanceandcell effectiveseriesresistance: |                                                                                                                                                                               |
| Warm-uptimeafter power-on:                                                              | 1hour                                                                                                                                                                         |
| Requiredisolationof DUTsacrosschannels:                                                 | ≥ 10M Ω                                                                                                                                                                       |
| Output leakagecurrent whenoff:                                                          | ≤ 1 μ A                                                                                                                                                                       |
| Enviro nmentalconditio ns:                                                              |                                                                                                                                                                               |
| Operating environment:                                                                  | Indoor use, insta llationcategoryII (for ACinput), pollutiondegree2                                                                                                           |
| Ambient temperaturerange:                                                               | 20°Cto30°C(maximumrate-of-change(dT /dt)must be<5°C/hour)                                                                                                                     |
| Relative humidity:                                                                      | Upto80%(non-condensing)                                                                                                                                                       |
| Altitude:                                                                               | Upto2000meters                                                                                                                                                                |
| Storage t mperature:                                                                    | -30°Cto70°C                                                                                                                                                                   |
| Digita l Port                                                                           |                                                                                                                                                                               |
| Max voltagerating:                                                                      | +16.5VDC /- 5VDCbetweenpins                                                                                                                                                   |
| Pins 1&2asFLT:                                                                          | Maximumlow-level output voltage=0.5V@4mA Maximumlow-level sinkcurrent=4mA Typical high-level leakagecurrent=1mA@16.5VDC                                                       |
| Pins 1-7asoutputs:                                                                      | Maximumlow-level output voltage=0.5V@4mA; 1V@50mA;1.75V@100mA Maximumlow-level sinkcurrent =100mA Typical high-level leakagecurrent=1mA@16.5VDC                               |
| Pins 1-7asinputs:                                                                       | Maximumlow-level input voltage=0.8V Minimumhigh-level input voltage=2V Typical low-level current =-2mA@0V(internal 2.2kpull-up) Typical high-level leakagecurrent=1mA@16.5VDC |
|                                                                                         | Pin8iscommon(internallyconnectedtochassisground)                                                                                                                              |
| Pin 8:                                                                                  |                                                                                                                                                                               |
| ACinput                                                                                 |                                                                                                                                                                               |
| Nominal rating:                                                                         | 100-120,200-240VAC ;50/60Hz                                                                                                                                                   |
| Input voltagerange:                                                                     | ±10%ofnominal rating                                                                                                                                                          |
| Power consumption:                                                                      | 150VAMax                                                                                                                                                                      |

## External Temperature Measurement

The external temperature sensor input on the rear panel requires an external 10 k Ω thermistor.

| Measurement Input                                     | Characteristic                                                                                            |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Thermistor Requirements:                              | NegativeT emperaturecoefficient (NT C) 10k Ω Nominal Resistanceat 25°C ProgrammableBetavalue(4073default) |
| Temperaturemeasurement range:                         | -20°Cto100°C                                                                                              |
| Temperaturemeasurement uncertainty:                   | 0°Cto60°C±1.5°C 60°Cto100°C±4.0°C                                                                         |
| Total wiringresistance(sumof bothleads)toT hermistor: | ≤ 10 Ω                                                                                                    |

## Dimensionsand Weight

![Image](%20BT2152B-prg_artifacts/image_000018_f75fc41494f8bf9f3c7f1d392c48a0ff75be1ca1a81e29d847af85389048bea1.png)

Do not block the air intake at the front and side, or the exhaust at the rear of the instrument.

![Image](%20BT2152B-prg_artifacts/image_000019_993d28924132d5e680b6da3d31892c6828ddebe301a83cf06e68315e362fbccd.png)

- l The front air inlet requires a minimum of 6 inches (15 cm) clearance. Inlet air temperature must be within the temperature range of 20°Cto 30°C.
- l The rear air outlet requires a minimum of 6 inches (15 cm) clearance.
- l The small air outlet on the left side of the unit must also be unrestricted, with a minimum clearance of 1.25 inches (30 mm) or more. Clearance to the instrument support rail could be as small as 10 mm if rack mounted.
- l The instrument should not be installed in a pressured rack or enclosure.

## Weight

10.2 kg ((22.5 lbs.)

## CommandQuick Reference

## CALibration

:DATE &lt; date &gt;

:END

:LOAD

:RESult? &lt; value &gt;

:SECure

:CODE &lt; code &gt;

:STATe 0|OFF|1|ON

:STARt

:STEP &lt; step &gt;

:STORe

:STRing &lt; string &gt;

:VALue? &lt; step &gt;

:VERification

:END

:STARt &lt; channel &gt;

:VOLTage &lt; voltage &gt;

:MEASure

:WIRE

:RESistance

:AUTO

:BYSHort

:CLEar

:LOAD &lt; value &gt;

:SAVE &lt; value &gt;

| :DATE < date >                        | Sets the calibration date                            |
|---------------------------------------|------------------------------------------------------|
| :END                                  | Ends calibration                                     |
| :LOAD                                 | Loads the previous calibration values                |
| :RESult? < value >                    | Enters the resulting measurement for calibration     |
| :SECure                               |                                                      |
| :CODE < code >                        | Sets a calibration security code                     |
| :STATe 0&#124;OFF&#124;1&#124;ON      | Secures or unsecures calibration                     |
| :STARt                                | Initiates calibration                                |
| :STEP < step >                        | Steps through the reference calibration processes    |
| :STORe                                | Stores the cal constants in theEEPROM                |
| :STRing < string >                    | Stores a message in calibration memory               |
| :VALue? < step >                      | Returns the calibration constants of the step        |
| :VERification                         |                                                      |
| :END                                  | Ends the verification process                        |
| :STARt < channel >                    | Starts the verification process                      |
| :VOLTage < voltage >                  | Enters the output voltage for verification           |
| :MEASure                              |                                                      |
| :INITiate < time >, < tint >          | Starts a verification measurement                    |
| :WIRE                                 |                                                      |
| :RESistance                           |                                                      |
| :AUTO                                 | Runs wire resistance calibration with wires shorted  |
| :BYSHort                              | Runs wire resistance calibration with wires shorted  |
| :CLEar                                | Resets all wiring resistance values to zero          |
| :INSitu (@<chanlist>)                 | Runs wire resistance calibration with cells in place |
| :LOAD < value >                       | Loads the wiring resistance values from a file       |
| <:SAVE value >                        | Saves the wiring resistance values to a file         |
| :VALues < resistance >, (@<chanlist>) | Manually sets the wire resistance values             |

## Common Commands

| ABORt       | Aborts the measurement in progress                                     |
|-------------|------------------------------------------------------------------------|
| *CAL?       | Initiates auto-calibration on all channels                             |
| *CLS        | Clears status                                                          |
| *ESE <mask> | Standard Event StatusEnableCommand                                     |
| *ESE?       | Standard Event Status Enable Query                                     |
| *ESR?       | Standard Event Status Register Query                                   |
| *IDN?       | Returns instrument identification                                      |
| *OPC?       | Returns "1" to the output buffer when all pending operations complete  |
| *RST        | Resets the instrument. These settings are described under Reset State. |
| *STB?       | Status byte query                                                      |
| *TST?       | Self-test query                                                        |
| *WAI        | Pausescommand processing until all pending operations are complete     |

## CONFigure

:INSitu

:CURRent HIGH|MED|LOW

:TEST:WIRE

:RESistance 5|10|20|&lt; value &gt;

:RESistance?

Selects the current level used during in situ calibration Sets wiring resistance for use on all channels

Returns either 5, 10, or 20

## [SOURce:]DIGital

[SOURce:] is optional

:INPut

:DATA?

Reads the state of the digital control port

:OUTPut

:DATA &lt; value &gt;

Sets the state of the digital control port

:PIN&lt;17&gt;

:FUNCtion DIO|DINPut|FAULt|INHibit Specifies the pin function

:POLarity POSitive|NEGative Specifies the pin polarity

## FETCh

:CURRent

:LATest? (@&lt;chanlist&gt;)

:LOG? &lt; values/ chan &gt; [,&lt; offset/ chan &gt;],

(@&lt;chanlist&gt;)

:BINary? &lt; values/ chan &gt;, (@&lt;chanlist&gt;)

Returns the most recent measurements Returns the measurement log in ASCII

Returns the measurement log in binary

:POINts?

Returns the number of readings available

:MEDian

:FIT?

:LOG?

&lt;

values/ chan

&gt; [,&lt;

(@&lt;chanlist&gt;)

:BINary?

&lt;

values/ chan Returns the median fit log in ASCII

offset/ chan

&gt;],

&gt;, (@&lt;chanlist&gt;)

Returns the median fit log in binary

```
:POINts? Returns the number of readings available :SUBTraction :LOG? < values/ chan > [,< offset/ chan >], (@<chanlist>) Returns the median subtraction log in ASCII :BINary? < values/ chan >, (@<chanlist>) Returns the median subtraction log in binary :POINts? Returns the number of readings available :PROBecheck? (@<chanlist>) Returns results of the probe check test :TEMPerature :LATest? Returns the most recent temperature :LOG? < values > [,< offset >] Returns the temperature log in ASCII :LOG :BINary? < values > Returns the temperature log in binary :POINts? Returns the number of readings available :VOLTage :LATest? (@<chanlist>) Returns the most recent measurements :LOG? < values/ chan > [,< offset/ chan >], (@<chanlist>) Returns the measurement log in ASCII :LOG :BINary? < values/ chan >, (@<chanlist>) Returns the measurement log in binary :POINts? Returns the number of readings available :OCV? (@<chanlist>) Retrieves the open-circuit voltage values FORMat :BORDer NORM|SWAP Selects the byte order for binary block transfers INITiate :TEST :MATChed <time><units>, <ovp>, <uvp>, <res> [,<tint>[,<curr>[,<ocp>]]], (@<chanlist>) Sets parameters for the voltage matched discharge current measurement :OCV (@<chanlist>) Initiates an open-circuit voltage test :PROBecheck (@<chanlist>) Initiates a probe check test LXI :IDENtify [:STATe] 0|OFF|1|ON Turns the front panel LXI identify indicator on or off OUTPut :INHibit :MODE LATChing|LIVE|OFF Sets the operating mode of the Inhibit Input digital pin :PROTection :CLEar Resets any protection events that have occurred
```

## SENSe

:OCV

:AVAIlable?

:PROBecheck

:AVAIlable?

:THERmistor

:TTIMe

:REMaining?

:VERification

:AVAIlable?

:WIRE

:RESistance

:AVAIlable?

| :OCV :AVAIlable?                                                                         | Returns availability of the OCVmeasurement           |
|------------------------------------------------------------------------------------------|------------------------------------------------------|
| :PROBecheck                                                                              |                                                      |
| :AVAIlable?                                                                              | Returns availability of the probe check test         |
| :THERmistor                                                                              |                                                      |
| :CONFigure < temp >, < resistance >, < beta >                                            | Specifies parameters for the external thermistor     |
| :TTIMe                                                                                   |                                                      |
| :REMaining?                                                                              | Returns the remaining time for the present test      |
| :VERification                                                                            |                                                      |
| :AVAIlable?                                                                              | Returns availability of the calibration verification |
| :WIRE                                                                                    |                                                      |
| :RESistance                                                                              |                                                      |
| :AVAIlable?                                                                              | Returns availability of the wire resistance values   |
| :CONFigure < resistance >, (@<chanlist>) Specifies the wiring resistance of each channel |                                                      |

## STATus

:ALARm

:CONDition?

:CURRent?

:VOLTage?

:ENABle &lt; value &gt;

:OPERation

:CONDition?

:ENABle &lt; value &gt;

| :ALARm            |                                                    |
|-------------------|----------------------------------------------------|
| [:EVENt]?         | Queries the alarm event register                   |
| :CONDition?       | Queries the alarm condition register               |
| :CURRent?         | Returns thesum of the over-current condition bits  |
| :VOLTage?         | Returns thesum of the over-voltage condition bits  |
| :UNDer?           | Returns thesum of the under-voltage condition bits |
| :ENABle < value > | Sets the alarm enable register.                    |
| :OPERation        |                                                    |
| [:EVENt]?         | Queries the operation event register               |
| :CONDition?       | Queries the operation condition register           |
| :ENABle < value > | Sets the operation enable register                 |

## SYSTem

## :COMMunicate

:LAN

:CONTrol?

:DHCP 0|OFF|1|ON

:DOMain?

:MAC?

:SMASk "&lt; mask &gt;"

:TELNet

:UPDate

:ERRor?

:LICense

:CATalog?

:TIME &lt; hh &gt;, &lt; mm &gt;, &lt; ss &gt;

:TEMPerature?

| :COMMunicate :ENABle 0&#124;OFF&#124;1&#124;ON < interface >   | Enables or disables the remote interface         |
|----------------------------------------------------------------|--------------------------------------------------|
| :LAN                                                           |                                                  |
| :CONTrol?                                                      | Reads the initial control connection port number |
| :DHCP 0&#124;OFF&#124;1&#124;ON                                | Enables or disablesDHCP                          |
| [1&#124;2]:DNS "< address >"                                   | Assigns static IPaddresses of DNSservers         |
| :DOMain?                                                       | Returns the domain name                          |
| :GATeway "< address >"                                         | Assigns a default gateway address                |
| :HOSTname "< name >"                                           | Assigns a hostname                               |
| :IPADdress "< name >"                                          | Assigns a static IPaddress                       |
| :MAC?                                                          | Returns the instrument'sMACaddress               |
| :SMASk "< mask >"                                              | Assigns a subnet mask                            |
| :TELNet                                                        |                                                  |
| :PROMpt "< string >"                                           | Setsthecommand prompt for Telnet                 |
| :WMESsage "< string >"                                         | Sets the welcome message for Telnet              |
| :UPDate                                                        | Saves any changesmadeto theLAN settings          |
| :WINS [1&#124;2] "< address >"                                 | Assigns the static IPaddresses of WINSservers    |
| :DATE < yyyy >, < mm >, < dd >                                 | Sets the date of the system clock                |
| :ERRor?                                                        | Reads and clears one error from the error queue  |
| :LICense                                                       | Reads and clears one error from the error queue  |
| :CATalog?                                                      | Returns the channel license of the unit          |
| :TIME < hh >, < mm >, < ss >                                   | Sets the time of the system clock                |
| :TEMPerature?                                                  | Returns the external sensor'stemperature value   |

![Image](%20BT2152B-prg_artifacts/image_000020_b21ff9e84a8c9b3e139ab9e0a8d06f53b01311c76dadb725f580ce50e5dfa95e.png)

## 2 Installing the Analyzer

Before Installation

Connect the Power Cord

Connect the Interfaces

Connect the Cell Cables

## Before Installation

## Inspect the Unit

When you receive your Keysight BT2152A/B Self-Discharge Analyzer, inspect it for any obvious damagethat may have occurred during shipment. If there is damage, notify the shipping carrier and nearest Keysight Sales and Support Office immediately. Refer to www.keysight.com/find/ assist.

Until you have checked out the unit, save the shipping carton and packing materials in case the unit has to be returned.

## Check for Items Supplied

Before getting started, check the following list and verify that you have received these items. Referto the box packing list for any additional items that may be included with your shipment. If anything is missing, please contact your nearest Keysight Sales and Support Office.

| BT2152A /BItems        | Description                                                             | PartNumber                                  |
|------------------------|-------------------------------------------------------------------------|---------------------------------------------|
| Power cord             | Apower cordsuitablefor your location                                    | Call Keysight Sales&Support Office          |
| LANcable               | LANinterfacecable- cableisinstalledonBT 2152A                           | Keysight 8121-3010 L-COMTRD815OR-7          |
| Digita l connector     | 8-pinconnector for thedigital port                                      | Keysight 1253-6408; PhoenixC ontact 1840421 |
| Thermistor connector   | 2-pinconnector for anexternal thermistor                                | Keysight 0360-3009 PhoenixC ontact 1840366  |
| Calibrationconnector   | 3-pinconnector for ancalibrationconnections                             | Keysight 0360-3038 PhoenixC ontact 1840379  |
| Thermistor cable       | 2-meter cablewith10kthermistor - usedwiththermistor connector 0360-3009 | Keysight BT2152-61607                       |
| Safetybooklet          | Includessafetyinformation                                               | Keysight 9320-6797                          |
| Calibrationcertificate | Calibrationcertificatereferencedtoserial number                         | None                                        |

## Accessories

| Acces sory   | Description                                                          |
|--------------|----------------------------------------------------------------------|
| BT2152-60002 | Verifica tionkit for BT2152Aonly- tosimplifyinstrument verifica tion |
| BT2180A      | Breakout boardfor BT2152Bonly- DB37(female)toscrew-terminals         |
| BT2181A      | 2-meter cablefor BT2152Bonly- DB37(male)toDB37(male)                 |
| BT2182A      | 4-meter cablefor BT2152Bonly- DB37(male)toDB37(male)                 |
| BT2183A      | Verifica tionfixturefor BT2152Bonly                                  |
| BT2184A      | Rackmount kit without handlesfor BT2152Bonly                         |

The following figure provides details about the breakout board accessory.

![Image](%20BT2152B-prg_artifacts/image_000021_fff2b633e068f45d1beb35e6ab91c36bbb6c45c79b14338568c8f133650b9a8f.png)

## Review Safety Information

This instrument is a Safety Class 1 instrument, which means it has a protective earth terminal. That terminal must be connected to earth ground through a power source equipped with an earth ground. Refer to the Safety Notices page for general safety information. Before installation or operation, check the instrument and review this guide for safety warnings and instructions. Safety warnings for specific procedures are located at appropriate places throughout this guide.

## Observe Environmental Conditions

![Image](%20BT2152B-prg_artifacts/image_000022_4225583a425470e94c3eae8f55373315253d4e1a0bfa457600ca99c94f96f5ba.png)

Donot operate the instrument in the presence of flammable gasesor fumes.

The environmental conditions of the instrument are documented under Characteristics. The unit should only be operated indoors in a controlled environment. Do not operate the unit in areas where the ambient temperature is outside the 20°Cto 30°Crange.

## Provide Adequate Air Flow

![Image](%20BT2152B-prg_artifacts/image_000023_66d2de2ad55820e4bca49391e916f82d290c4095e696d5062c3ae2d7a4b5a0a3.png)

Do not block the air intake at the front and side, or the exhaust at the rear of the instrument.

The dimensions of your instrument as well as an outline diagram are given under Dimensions. Fans cool the unit by drawing air through the front and exhausting it out the side and back. The unit must be installed in a location that allows sufficient space of at least 6 inches (15 cm) at the front and back of the unit for adequate air circulation. The small air outlet on the left side of the unit must also be unrestricted, with a minimum clearance of 1.25 inches (30 mm) or more.

## Connect the Power Cord

## [WARNING](warning.gif)

FIREHAZARDUseonlythepowercordthat wassuppliedwithyour instrument. Using other typesof power cordsmaycause overheating of the power cord, resulting in fire.

SHOCKHAZARDThepowercordprovidesachassisgroundthrougha thirdconductor. Ensure that your power outlet isof the three-conductor type with the correct pin connected toearth ground.

Connect the power cord to the AC Input Connector on the rear of the unit. If the wrong power cord was shipped with your unit, contact your nearest Keysight Sales and Support Office.

The ACinput on the back of your unit is a universal AC input. It accepts nominal line voltages in the range of 100 VACto 240 VAC. The frequency can be 50 Hz or 60 Hz.

![Image](%20BT2152B-prg_artifacts/image_000024_9f0856d6b7d7a3c74ab2fafa8a2217f67d1b201e8a791a61b82c2725d3960a66.png)

The detachable power cord may be used as an emergency disconnecting device. Removing the power cord will disconnect AC input power to the unit.

## Connect the Interfaces

LAN Connections

USBConnections

DIgital Port Connections

Thermistor Connections

If you have not already done so, install the Keysight IO Libraries Suite, which can be found at www.keysight.com/find/iolib .

![Image](%20BT2152B-prg_artifacts/image_000025_cb5c300084d03c4788e1a53cdbd49d4b7c4a8c231da5e3c7100930c0ff28c57f.png)

For detailed information about GPIB, USB, and LAN interface connections, refer to the documentation included with the Keysight IO Libraries Suite.

## LAN Connections

![Image](%20BT2152B-prg_artifacts/image_000026_38c521c9c7d01400bba80e2df6be762797730b1706f46a0bbe504b01a8c417db.png)

Equipment Damage Never insert any RJ45 cell cables into the LAN connector. The LAN and RJ45 terminals are NOT compatible.

1. Connect the instrument to the site LAN or to your computer using the LAN cable.

![Image](%20BT2152B-prg_artifacts/image_000027_2d1e5962d79cfda0438d80518dd9317f69a580a478699925a614623fe064289d.png)

For Keysight BT2152A, the LAN cable comes installed to prevent any cell cables from being accidentally inserted into the LAN connector. If you need to remove the LAN cable, insert a small screwdriver or equivalent into the hole and push down on the cable latch to release it.

![Image](%20BT2152B-prg_artifacts/image_000028_1d3a532e744ae7bc2714de3da49cff73cdddecd3fcd928b40cc758130223f99f.png)

2. The as-shipped LAN settings are configured to automatically obtain an IP address from the network using a DHCPserver (DHCPis set On). The DHCPserver will register the instrument'shostname with the dynamic DNSserver. The hostname as well as the IPaddress can then be used to communicate with the instrument. If you are using a private LAN, you can leave all LAN settings as they are. Most Keysight products and most computers will automatically choose an IPaddress using auto-IPif a DHCPserver is not present. Each assigns itself an IP address from the block 169.254.nnn. The frontpanel Lan indicator will come on when the LAN port has been configured.
3. Use the Connection Expert utility of the Keysight IOLibraries Suite to add the instrument and verify a connection. To add the instrument, you can request the Connection Expert to discover the instrument. If the instrument cannot be found, add the instrument using the instrument's hostname or IP address.
4. You can now use Interactive IOwithin the Connection Expert to communicate with your instrument, or program the instrument directly using the applicable SYSTem:COMMunicate:ENABle commands.

## USBConnections

1. Connect the instrument to the USB port on your computer using a customer-supplied USB cable. .
2. With the Connection Expert utility of the Keysight IOLibraries Suite running, the computer will automatically recognize the instrument. This may take several seconds. The computer will then display the VISA alias, IDN string, and VISA address. This information is located in the USB folder.
3. You can now use Interactive IOwithin the Connection Expert to communicate with your instrument, or program the instrument directly using the applicable SYSTem:COMMunicate:ENABle commands.

## Digital Port Connections

![Image](%20BT2152B-prg_artifacts/image_000029_4ace58b0293c8ea4a99b418d3c88402f1dc19aef6bde72f5de3df0f79f327e1a.png)

Twist and shield all signal wires to and from the digital connector. With shielded wire, connect only one end of the shield to chassis ground to prevent ground loops.

An 8-pin connector and a quick-disconnect connector plug are provided for accessing the digital port functions. Refer to Items Supplied for part numbers. Disconnect the connector plug to make your wire connections. The connector plug accepts wires sizes from AWG14 (1.5 mm 2 ) to AWG28 (0.14 mm 2 ). Strip the wire insulation back 7 mm.

![Image](%20BT2152B-prg_artifacts/image_000030_fc493cd6a79546cb4e4547199dcbbf1ca22a5781110513a080f65a52ce1f611b.png)

1. Insert wires
2.    Tighten screws
3. Fault/ Inhibit configurable pins (observe INH polarity)
4. Digital IO-configurable pins
5.    Signal common

Information on using the digital port is found under Understanding the Digital Port. The electrical characteristics are described under Common Characteristics.

## Thermistor Connections

A2-pin connector and a quick-disconnect connector plug are provided for the thermistor connections. Usethe provided thermistor cable. Refer to Items Supplied for the thermistor cable part number.

![Image](%20BT2152B-prg_artifacts/image_000031_f5819afd7a40e291ad01c9fc225bb22f533c2a699d0624fc105b86c0f22babb8.png)

![Image](%20BT2152B-prg_artifacts/image_000032_56b9fa89679125ad91708349a43bdbee1c0c6860939beb6e1f7b85794f8e746f.png)

1. Insert wires
2.    Tighten screws

Equipment Damage The thermistor connection to the cell must be insulated. The thermistor cannot touch earth ground or the plus and minus cell terminals.

The thermistor provided with the cable is Keysight p/n 0837-4194; Amphenol Advanced Sensors RL1005-5744-103-SA. Refer to SENse:THERmistor:CONFigure for additional information. Other Negative Temperature Coefficient (NTC) thermistors are supported but these are required to have a nominal resistance of 10 k Ω at a nominal temperature of 25°C. Other NTC sensor's beta values will result in different accuracies. Contact Keysight Technologies for assistance.

## Connect the Cell Cables

ToKeysight Model BT2152A

ToKeysight Model BT2152B

This section describes how to make and connect the cell cables.

## ToKeysight Model BT2152A

Two methodsof cabling are available:

## 1. RJ45 to bare wire

Obtain off-the-shelf RJ45 CAT6+ shielded cables. Many lengths are available. For example: Manufacturer = Belden. Part number = C6F1106010. Maximum allowable cable length = 10 meters.

Cut the cable in the middle. Now, you have two pieces half the previous length. Each piece has an RJ45 on one side and bare wires on the other.

Connect the RJ45 CAT6+ cables from the instrument to the test fixture.

![Image](%20BT2152B-prg_artifacts/image_000033_ed8af22d4e62067c4c32a8c45c16ddd9f2a7045a34228a6aff5d6b88d8adff89.png)

NOTE

## 2. RJ45 to RJ45

Obtain off-the-shelf RJ45 CAT6+ shielded cables. Many lengths are available. For example: Manufacturer = Belden. Part number = C6F1106010. Maximum allowable cable length = 25 meters.

Obtain off-the-shelf RJ45 board mount receptacles. For example: Manufacturer = Amphenol. Part number = RJSSE-5380-04.

Mount the RJ45 receptacle on the test fixture. Connect the RJ45 CAT6+ cables from the instrument to the receptacle.

When using shielded cables like Cat 6A or Cat 7, leave the shield floating at the cell end of the cable. The cable shield connects to the instrument chassis at the BT2152A end of the cable.

Wire resistance calibration is recommended when all RJ45 cables have been installed in the instrument to allow for more accurate output resistance selections. Wire resistance calibration is also recommended whenever any RJ45 connector is unplugged, reinserted, or reseated. Wire resistance must be between 0Ω and 5Ω.

![Image](%20BT2152B-prg_artifacts/image_000034_0e0e4f88121d42df8407662800117f62107ee6ff0cea268d400e17a7a6f85757.png)

NOTE

When using shielded cables like Cat 6A or Cat 7, leave the shield floating at the cell end of the cable. The cable shield connects to the instrument chassis at the BT2152A end of the cable.

Wire resistance calibration is recommended when all RJ45 cables have been installed in the instrument to allow for more accurate output resistance selections. Wire resistance calibration is also recommended whenever any RJ45 connector is unplugged, reinserted, or reseated. Wire resistance must be between 0Ω and 5Ω.

## RJ45 WIre Color Codesand Pinout Numbers

The following figures illustrate the color codes and pin-outs of two types of RJ45 connectors, as viewed from the bottom of the connector.

![Image](%20BT2152B-prg_artifacts/image_000035_b79f43405581b283a50ed3cc31a176571edf8e3c55b65a654fd2e9370fcb31a4.png)

The following table shows the mapping of the color-coded wires into both T-568A and T-568B connectors. The table also shows the channel-assignment mapping of channels 1 through 4.

![Image](%20BT2152B-prg_artifacts/image_000036_102f590d6074fcc88884f2860e6c69e008f16e6b21b9b30da821dcc1023f76ab.png)

|              | RJ45 Pin8   | RJ45 Pin7   | RJ45 Pin6   | RJ45 Pin5   | RJ45 Pin4   | RJ45 Pin3   | RJ45 Pin2   | RJ45 Pin1   |
|--------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| Channels1to4 | -1          | +1          | -3          | -2          | +2          | +3          | -4          | +4          |
| T- 568A      | brown       | wht/brn     | orange      | wht/blu     | blue        | wht/org     | green       | wht/grn     |
| T- 568B      | brown       | wht/brn     | green       | wht/blu     | blue        | wht/grn     | orange      | wht/org     |

## 32-Channel Mapping to RJ45 Connectors

![Image](%20BT2152B-prg_artifacts/image_000037_4e23ec39ea695a9a4dfbdb7161d2505394589bc2a4f7099eedc995fab60f03e3.png)

Equipment Damage Do not connect any channel wires to earth ground.

The following figure shows the channel assignments for the 32-channel self-discharge analyzer.

Connector

Channel

![Image](%20BT2152B-prg_artifacts/image_000038_5aeed8402ef52565f73620e201b15ce2fbc3f8e679f1ace99e93bbb269da867b.png)

17-20 21-24 25-28 29-32

![Image](%20BT2152B-prg_artifacts/image_000039_dc6fa9aa6720c03fe50d021d9f0dd4d0b1d4130a5f66de7065a67ab96e01549d.png)

The following table shows the channel-assignment mapping of all 32 channels.

![Image](%20BT2152B-prg_artifacts/image_000040_82990027be83afdae7ff6773403a3ea330f85e4f0fd6b5e3cfe50a54d8092869.png)

|                        |   RJ45 Pin8 |   RJ45 Pin7 |   RJ45 Pin6 |   RJ45 Pin5 |   RJ45 Pin4 |   RJ45 Pin3 |   RJ45 Pin2 |   RJ45 Pin1 |
|------------------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| RJ45#1- channels1to4   |          -1 |          +1 |          -3 |          -2 |          +2 |          +3 |          -4 |          +4 |
| RJ45#2- channels5to8   |          -5 |          +5 |          -7 |          -6 |          +6 |          +7 |          -8 |          +8 |
| RJ45#3- channels9to12  |          -9 |          +9 |         -11 |         -10 |         +10 |         +11 |         -12 |         +12 |
| RJ45#4- channels13to16 |         -13 |         +13 |         -15 |         -14 |         +14 |         +15 |         -16 |         +16 |
| RJ45#5- channels17to20 |         -17 |         +17 |         -19 |         -18 |         +18 |         +19 |         -20 |         +20 |
| RJ45#6-channels21to24  |         -21 |         +21 |         -23 |         -22 |         +22 |         +23 |         -24 |         +24 |
| RJ45#7- channels25to28 |         -25 |         +25 |         -27 |         -26 |         +26 |         +27 |         -28 |         +28 |
| RJ45#8- channels29to32 |         -29 |         +29 |         -31 |         -30 |         +30 |         +31 |         -32 |         +32 |

## ToKeysight Model BT2152B

For best measurement results, Keysight recommends using cables with the following characteristics, which are built into the BT2181A and BT2182A cables (see Accessories).

- l Use twisted pairs of wires for each channel for as much of the distance from analyzer to cell as possible.
- l The bundle of the twisted pairs should be shielded, with a separate braided shield around the bundle.
- l The braid should be connected to the DB37 connector housings.
- l The DB37 male connectors should have machined (not stamped) pins.

The following cabling methods are recommended:

## 1. Accessory cables and breakout board

Asshown in the following figure, BT2180A breakout boards can be used in conjunction with the BT2181Aand BT2182Aaccessory cables (see Accessories). This is the preferred connection method. Each breakout board has a 37-pin D Subminiature female receptacle connected to two 16-pin screw terminal connectors. Cell wire harnesses can easily be connected to the breakout board with tywraps using the three strain relief mounting holes provided.

The breakout board screw terminals accept 16 AWGto 30 AWGwire sizes.

![Image](%20BT2152B-prg_artifacts/image_000041_265504e5cffd63261c4e6cfc9886b899972ca79f96c9c108d0bcabd44ea93f34.png)

## 2. 37-pin connector cables, male-to-male

Obtain or fabricate male-to-male 37-pin D subminiature cables that comply with the previously stated cable characteristics. You may wish to inquire about the following vendor's cables and parts:

| Cable, 18-twisted-pair 24 AWG, tinned stranded copper, with aluminum polyester shield plus braided tinned copper shield   | Belden 8348         |
|---------------------------------------------------------------------------------------------------------------------------|---------------------|
| Connector hood, top entry, metal                                                                                          | Harting 09670370344 |
| DB37 (m) Connector, solder cup, turned contacts                                                                           | Harting 09670375615 |

You can also obtain 2- and 4-meter cables that comply with the stated characteristics by ordering modelsBT2181Aand BT2182A(see Accessories).

Connect one end of the cable to the BT2152B. Connect the other end of the cable to the DB37 receptacle on the customer-supplied test fixture. Cell connections are wired to the test fixture.

![Image](%20BT2152B-prg_artifacts/image_000042_f7505cd6c0bbd31b01db8e1b8a9965c600f9b1bc980db5227041140fef14330b.png)

## 3. 37-pin connector cables, male-to-bare wire

Obtain male-to-unterminasted 37-pin D subminiature cables. The maximum allowable cable length is 10 meters. For best measurement results, all cabling must comply with the previously stated cabling characteristics.

Connect the DB37 cable connector to the BT2152B. Connect the unterminated wires to the cells in the test fixture.

![Image](%20BT2152B-prg_artifacts/image_000043_aa3afe05c225ce8da3f0559db0aa859f02de5af6ddb65003a56d4065473e6531.png)

## 32-Channel Mapping to 37-pin D Subminiature Connectors

![Image](%20BT2152B-prg_artifacts/image_000044_4d6e69fbb5e53dbced80b263d9d01ae814a3201b370472de8f0cb94d350acf81.png)

Equipment Damage Do not connect any channel wires to earth ground.

Connector pins as viewed from the rear panel of the instrument. Pin numbers on the 2- and 4- meter accessory cables are reversed.

## 2 Installing the Analyzer

![Image](%20BT2152B-prg_artifacts/image_000045_8123aa2178757c722e144865756a4661178520b0cf282a8692468f25f51aaa60.png)

![Image](%20BT2152B-prg_artifacts/image_000046_a1d321b38963690bbba6ca7bf91ee2424a5be554c9897823ae0cdd2ef9f161d1.png)

![Image](%20BT2152B-prg_artifacts/image_000047_ab4a9845611a7fa2a9919bb59b5a1fe443bbf003a9c793a05547a109f2cd9ce1.png)

Connector pins 3, 2, 1, 21, and 20 are not used. Do not make any connection to these pins. Just leave them floating, open, and disconnected

| "A "connectorchannels   | "A "connectorchannels   |   "A "connectorchannels | "A "connectorchannels   | "A "connectorchannels   |   "A "connectorchannels |   "A "connectorchannels | "A "connectorchannels   |   "A "connectorchannels | "A "connectorchannels   |   "A "connectorchannels | "A "connectorchannels   |   "A "connectorchannels |   "A "connectorchannels | "A "connectorchannels   |
|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
| Channels                | 1                       |                       2 | 3 4                     | 5                       |                       6 |                       7 | 8                       |                       9 | 10                      |                      11 | 12 13                   |                      14 |                      15 | 16                      |
| HIG Hpin                | 19 18                   |                      17 | 16                      | 15 14                   |                         |                      13 | 12 11                   |                         | 10 9                    |                       8 | 7                       |                       6 |                       5 | 4                       |
| 37                      | 36                      |                      35 | 34                      | 33                      |                      32 |                      31 | 30                      |                      29 | 28 27                   |                      26 | 25                      |                      24 |                      23 | LOWpin 22               |

|          | "B "connectorchannels   |   "B "connectorchannels |   "B "connectorchannels |   "B "connectorchannels |   "B "connectorchannels |   "B "connectorchannels |   "B "connectorchannels | "B "connectorchannels   |   "B "connectorchannels |   "B "connectorchannels |   "B "connectorchannels | "B "connectorchannels   |   "B "connectorchannels |   "B "connectorchannels | "B "connectorchannels   |
|----------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
| Channels | 17                      |                      18 |                      19 |                      20 |                      21 |                      22 |                      23 | 24                      |                      25 |                      26 |                      27 | 28 29                   |                      30 |                      31 | 32                      |
| HIG Hpin | 19 18                   |                      17 |                      16 |                      15 |                      14 |                         |                      13 | 12 11                   |                      10 |                       9 |                       8 | 7                       |                       6 |                       5 | 4                       |
| 37       | 36                      |                      35 |                      34 |                         |                      33 |                      32 |                      31 | 30 29                   |                      28 |                      27 |                      26 | 25                      |                      24 |                      23 | LOWpin 22               |

![Image](%20BT2152B-prg_artifacts/image_000048_b21ff9e84a8c9b3e139ab9e0a8d06f53b01311c76dadb725f580ce50e5dfa95e.png)

## 3 Operating the Analyzer

Understanding Front Panel Operation

Understanding the Digital Port

Using the Web Interface Cell Testing Tips and Best Practices

## Understanding Front Panel Operation

What Happensat power-on?

What happenswhen a test isinitiated?

What happenswhen a test stops?

What happenswhen the reference temperature exceedsitsspecification?

What happenswhen a protection event or error occurs?

The following indicators and controls are on the front panel.

![Image](%20BT2152B-prg_artifacts/image_000049_88b53fe2af0a822158664a6048b092d786997fd5c073011f0f54b5c8093aa844.png)

![Image](%20BT2152B-prg_artifacts/image_000050_add61f570cc5d677ac7c338d2c6572c5b88b21c8cfbb225190b01f8ea6b4bccd.png)

The AUX button is not active, and is reserved for future use.

## What happensat power-on?

Turn the unit on with the front-panel Line switch.

![Image](%20BT2152B-prg_artifacts/image_000051_cb5c300084d03c4788e1a53cdbd49d4b7c4a8c231da5e3c7100930c0ff28c57f.png)

It may take about 60 seconds or so for the unit to completely boot up.

When the unit is first turned on, the Power light turns green, indicating that power is on.

The LAN light turns green when the LAN connection is active. Flashing green indicates an active LXI identification state. Red indicates the LAN is disconnected. Pressing the LAN reset button on the front panel will attempt to restore the LAN connection. If this does not work, restoring LAN communication must be done using the test program.

The Ready light turns orange, indicating that the unit is warming up. A warm up time of about 1 hour is required for the unit to meet its specified performance. It is possible to send commands and operate the unit during the warm up time, but it is advisable to allow the unit to fully warm up before running any test. If, after warmup, power is cycled off for less than 5 minutes and then restored, the subsequent warm up will be shortened to about 30 minutes.

![Image](%20BT2152B-prg_artifacts/image_000052_26cbfb1fa18d740a38696e7281478ba604ed2b872e7395738a2d788a93d89ad5.png)

The Ready status is driven by elapsed time. If the unit is powered off and then powered on again, the Ready light will again turn orange for about one hour.

The Test and Error lights should be off. If the Error light is red, either a protection event, inhibit, or error has occurred (see What happens when a protection event or error occurs?).

## What happenswhen a test isinitiated?

Before initiating a test, wait for the Ready light to change from orange to green, which means the unit is warmed up and ready for testing. It is possible to send commands and operate the unit prior to the light changing to green, but it is advisable to let the unit warm up to meet specified performance.

The LAN light flashes blue when any SCPI commands or queries are sent.

The Test light flashes blue when the cell matching process has been initiated and is running.

The Test light stops flashing and turns solid blue when the cell measurement test is running and data logging is occurring.

The Test light turns off when the measurement logging has completed.

## What happenswhen a test stops?

Normally, a test runs for the duration of its programmed test time and then stops. A test can also be stopped before the completion of its programmed time by pushing the Stop button or sending an ABORt command. The stop button must be held for 1 second to abort the current test.

When a test stops or is stopped, the Test light turns off. The Power , LAN , and Ready lights are green. The Error light is off.

## What happenswhen the reference temperature exceedsitsspecification?

The Ready light turns orange when the internal reference temperature is slightly out of regulation. There may be a problem with the airflow. Check that the airflow at the vents is unobstructed. Once the internal temperature is restored, the Ready light will turn to green.

The Ready light flashes red when the internal reference temperature has increased to where damage could occur. When this happens the internal heaters are disabled and the operating temperature range will not be maintained. Turn the unit off, let it cool down, then turn it on to clear the condition.

## What happenswhen a protection event, inhibit, or error occurs?

The Error light turns red when a protection event, external inhibit, or error has occurred.

If a protection event occurs on a channel, that channel is disconnected from the cell. You can continue running the test on other channels. The channel that tripped protection remains disconnected from the cell until protection is cleared.

If an external inhibit occurs, all channels will be disconnected from the cells.

If an error occurs, the instrument will continue to operate with errors present.

Clearing these conditions can only be done with the test program by sending the OUTPut:PROTection:CLEar command. There is no front panel control to clear a protection event, inhibit, or error. Once the test program clears these events, the Error light turns off.

## Understanding the Digital Port

Digital Control Port

Bi-Directional Digital I/ O

Digital Input only

Fault Output

Inhibit Input

Coordinating Initiate Commands

Fault/ Inhibit System Protection

## Digital Control Port

ADigital Control Port consisting of seven I/ Opins is provided to access various control functions. Each pin is user-configurable.

The following table describes the possible pin configuration for the digital port functions. For a complete description of the electrical characteristics of the digital control port, refer to the Characteristics section.

| Function   | Description                                                                                                                                                                               |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DIO        | General-purposeground-referenceddigital input/output function.Theoutput canbeset with [SOURce:]DIG ital:O UTPut:DA TA.                                                                    |
| DINPut     | Digita l input-onlymode. Thedigital output dataof thepinisignored.                                                                                                                        |
| FAULt      | Appliesonlytopins1and2.P in1functionsasanisolatedfault output.Pin2servesastheisolatedcommon for pin1. Thefault signal istruewhenafault conditionoccursontheinstrument.Whenpin1isset tothe |
|            | FAULt function, theinstrument ignoresanycommandstoprogrampin2.Q ueriesof pin2will returnF AULt. If pin1ischangedfromFAULt toanother function,pin2isset toDINPut.                          |
| INHibit    | Appliesonlytopin3.W henpin3isconfiguredasaninhibit input; alogictruesignal at thepindisconnects all channelsfromthecells.                                                                 |
| Common     | Appliesonlytopin8.C onnectedtoground.                                                                                                                                                     |

In addition to the configurable pin functions, the logic polarity for each pin is also configurable. Positive uses a high-level voltage at the pin as true, active, or binary 1. Negative uses a low-level voltage at the pin as true, active, or binary 1.

## Bi-Directional Digital I/ O

Each of the seven pins can be configured as general purpose bi-directional digital inputs and outputs. The polarity of the pins can also be configured. Pin 8 is the signal common for the digital I/ O pins. Data is programmed according to the following bit assignments:

| Pin        | 7       |   6 |   5 |   4 |   3 |   2 | 1      |
|------------|---------|-----|-----|-----|-----|-----|--------|
| Bit Weight | 64(msb) |  32 |  16 |   8 |   4 |   2 | 1(lsb) |
| Bit Number | 6       |   5 |   4 |   3 |   2 |   1 | 0      |

The digital I/ O pin can be used to control both relay circuits as well as digital interface circuits. The following figure illustrates typical relay circuits as well as digital interface circuit connections using the digital I/ O functions

![Image](%20BT2152B-prg_artifacts/image_000053_55361087be098862ce208202797cdc30a9434aef4c6e411cd21382f07b8e893b.png)

To configure the pins for digital I/ O:

```
DIG:PIN1:FUNC DIO DIG:PIN2:FUNC DIO DIG:PIN3:FUNC DIO DIG:PIN4:FUNC DIO DIG:PIN5:FUNC DIO DIG:PIN6:FUNC DIO DIG:PIN7:FUNC DIO \\ sets the function for all 7 pins to digital IO DIG:PIN1:POL POS DIG:PIN2:POL POS DIG:PIN3:POL POS DIG:PIN4:POL POS DIG:PIN5:POL POS DIG:PIN6:POL POS DIG:PIN7:POL POS \\ sets the function for all 7 pins to positive DIG:OUTP:DATA 7 \\ configures pins 1 through 7 as '0000111'
```

## Digital Input

Each of the seven pins can be configured as digital input only. The polarity of the pins can also be configured. Pin 8 is the signal common for the digital input pins. The pin status reflects the true condition of the external signal that is applied to the pin. The pin state is not affected by the setting of DIGital:OUTPut:DATA.

To configure the pins for digital input only:

```
DIG:PIN1:FUNC DINP DIG:PIN2:FUNC DINP DIG:PIN3:FUNC DINP DIG:PIN4:FUNC DINP DIG:PIN5:FUNC DINP DIG:PIN6:FUNC DINP DIG:PIN7:FUNC DINP  \\ sets the function for all 7 pins to digital input DIG:PIN1:POL POS DIG:PIN2:POL POS DIG:PIN3:POL POS DIG:PIN4:POL POS DIG:PIN5:POL POS DIG:PIN6:POL POS DIG:PIN7:POL POS \\ sets the function for all 7 pins to positive DIG:INP:DATA? \\ reads the data on the pins
```

## Fault Output

Pins 1 and 2 can be configured as a fault-output pair. The Fault Output function enables a fault condition to generate a protection fault signal from the Alarm Status Group on the digital port.

Both pins 1 and 2 are dedicated to this function. Pin 1 is the Fault output; pin 2 is the common for pin 1. This provides for an optically-isolated output. The polarity of pin 1 can also be configured. When the pin polarity is positive, a fault condition causes the isolated output to conduct. Note that the Fault output signal remains latched until the fault condition is removed and the protection circuit is cleared using the OUTPut:PROTection:CLEar command.

![Image](%20BT2152B-prg_artifacts/image_000054_4ace58b0293c8ea4a99b418d3c88402f1dc19aef6bde72f5de3df0f79f327e1a.png)

Pin 2's selected function is ignored. Connect Pin 2 to the ground of the external circuit.

To configure the Fault Output function:

```
DIG:PIN1:FUNC FAUL \\ sets the function for pin 1 to fault output DIG:PIN1:POL POS \\ sets the function for pin 1 to positive
```

## Inhibit Input

Pin 3 can be configured as a remote inhibit input. The Inhibit input function lets an external inhibit signal disconnect all input channels from the cells. The Inhibit input is level triggered. The signal latency is 5 microseconds. Pin 8 is the common for pin 3. Use the OUTPut:INHibit:MODEcommand to specify the following Inhibit input modes: Latching, Live, or Off.

```
DIG:PIN3:FUNC INH \\ sets the function for pin 3 to inhibit input DIG:PIN3:POL POS \\ sets the polarity for pin 3 to positive OUTP:INH:MODE LIVE \\ sets the inhibit mode to Live
```

Note that the front panel Error light turns on when any inhibit signal (live or latched) occurs. To clear the Error light, remove the inhibit signal and send the OUTPut:PROTection:CLEar command.

## Synchronized Triggering for Calibrating Wire Resistance and Initiating Tests acrossMultiple BT2162BInstruments

The following example program allows multiple BT2162B units to operate synchronously. This is recommended for multiple BT2162B operation on a common DUT(series of cells or bipolar configuration). It allows for any BT2162B in the test system to act as the primary BT2162B. In the example program below, DUT1 is the Primary BT2162B. This is software selectable to allow for flexibility if a BT2162B unit is not connected to cells or removed from the test system. Instrument setup configurations are identical for each BT2162B (primary and secondaries) which simplifies the programming required. Additionally, each BT2162B's digital I/Oport is wired identically for ease of physical implementation.

The accompanying example program (written in MATLAB ® ) demonstrates the primary BT2162B receiving a software programmatic TRIGger command. This triggers the primary and immediately outputs a trigger pulse on TOUTput (pin 4) to the digital I/ O harness. This goes to TINPut (pin 7) on all secondary digital inputs, causing each BT2162B's to also trigger. Additionally, the trigger event for all BT2162B's can be controlled by the optional operator push button (see diagram below). The program assumesall channels have cells connected for each BT2162B. First it performs and checks for valid OCVresults on all channels. Then performs and checks for valid Insitu Cal results on all channels. If all checks pass, then the program Initiates SDM on all channels. Each one of these actions is performed using synchronous triggering.

![Image](%20BT2152B-prg_artifacts/image_000055_40b5442df97dd5af880a6cb0c3f17933c3369628b6025e942032e1beb7ccdf1d.png)

BT2162BDigital I/OTrigger Characteristics:

- - Trigger output pulse widths: 9 m s
- - Required trigger input pulse width &gt;5 m s
- - Primary to secondary Latency is negligible for multiple BT2162B synchronization and is &lt;10 ms

## Example program:

```
% --------------------------------------------------------------- % --------------------------------------------------------------- % This is a MATLAB program written to demonstrate BT2162B % synchronized triggering capability % % Version 1.0 % August 7th, 2024 % % --------------------------------------------------------------- % --------------------------------------------------------------- function Fluca2_MultiFlucaSyncSQ_customerMethod_FW_1_12 % --------------------------------------------------------------- % Setup Matlab space and clear any instrument io objects try newobjs = instrfind; if isempty(newobjs) == 0 fclose(newobjs); delete(newobjs); end clear newobjs; catch end fclose('all'); clear; close all; clc; format long; % --------------------------------------------------------------- % Define customer variables dut1 = visa('keysight','TCPIP0::169.254.139.226::inst0::INSTR'); % Primary dut2 = visa('keysight','USB0::0x2A8D::0x3502::US78990014::0::INSTR'); % Secondary 1 dut3 = visa('keysight','TCPIP0::169.254.139.224::inst0::INSTR'); % Secondary 2 chanList = '1:4'; BT2162B_Instruments = [ dut1 dut2 dut3 ]; % define the array of instruments % e.g. BT2162B_Instruments = [ dut1 dut2 ] % e.g. BT2162B_Instruments = [ dut1 dut2 dut3 dut4 dut5 ] % --------------------------------------------------------------- % Open BT2162B instrument i/o % This defines the variables dut1, dut2, etc, as instrument objects % It does not define 'dut' that's merely a loop variable. for dut = BT2162B_Instruments % for each BT2162B set(dut,'eosmode','read&write'); set(dut,'eoscharcode','lf'); set(dut,'timeout',20); % 20 second timeout set(dut,'InputBufferSize',2^22); set(dut,'OutputBufferSize',512); fopen(dut); end % --------------------------------------------------------------- % Initial setup % Applies to all BT2162B units (primary and secondaries) for dut = BT2162B_Instruments % for each BT2162B
```

```
fprintf(dut,'*RST'); fprintf(dut,'*CLS'); fprintf(dut,'CALibration:WIRE:RESistance:CLEar'); fprintf(dut,'CONFigure:INSitu:CURRent MED'); % LOW MED or HIGH fprintf(dut,'TRIG:SOURCE EXT'); fprintf(dut,'DIGital:PIN4:FUNCtion TOUTput'); fprintf(dut,'DIGital:PIN7:FUNCtion TINPut'); fprintf(dut,'DIG:PIN4:POL NEG'); fprintf(dut,'DIG:PIN7:POL NEG'); fprintf(dut,'OUTPut:TRIGger:STATe ON'); query(dut,'*OPC?'); % Wait for instrument to be done processing commands end % --------------------------------------------------------------- % Check Instrument FW and errors, HALT if any are found for dut = BT2162B_Instruments % for each BT2162B resp = query(dut,'*IDN?') if str2double(resp(44:48)) > 1.12 disp('Instrument FW supports this feature') else error('Instrument FW needs to be updated') end checkInstrumentErrors(dut) % function call to routine at end of program end % --------------------------------------------------------------- % OCV % --------------------------------------------------------------- % Detect cells, measure cell OCV on each channel for dut = BT2162B_Instruments % for each BT2162B fprintf(dut,['INIT:TEST:OCV 4.2, 2.8, 0.001, 10, (@' chanList ')']); end % --------------------------------------------------------------- % WAIT until all instruments are in 'wait for trigger' state % Check status operation condition 'wait for trigger' bit % bit 5 is the 6th bit (lsb), 1 = waiting for trigger, 0 = not waiting for dut = BT2162B_Instruments % for each BT2162B while 1 % Query the status operation condition register % Convert it to a binary number of at least 6 bits in length WaitForTrigger = dec2bin(str2double(query(dut,'STATus:OPERation:CONDition?')),6); % Check that bit 5 (6th bit) is a 1. % If so, move on to the next BT2162B. % If not, check again. if ( (str2double(WaitForTrigger(end-5)) == 1) ) % Bit 5 is 6th bit from end disp('correctly WAITING for a trigger') break % break out of while loop else % not yet waiting for trigger, must try again % can optionally insert a 1 second delay here. % Check for errors, HALT if any are found checkInstrumentErrors(dut) % function call to routine at end of program end end end % --------------------------------------------------------------- % Send a TRIG command to the primary BT2162B only fprintf(dut1,'TRIGger');
```

## 3 Operating the Analyzer

```
% Note this communication is with dut1 only, not dut2 or dut3 % This will trigger the primary, and % cause pin 4 on the primary to output a trigger pulse. % This will go to all secondary pin 7's (trigger inputs) % and will trigger those instruments. % Also note that *TRG will not trigger unless source is 'BUS' % Here it is 'EXT', so TRIGger command is needed. % --------------------------------------------------------------- % WAIT for results to be available, check them, and display for dut = BT2162B_Instruments % for each BT2162B while (1 ~= str2double(query(dut,'SENSe:OCV:AVAIlable?'))) % Check for errors, HALT if any are found checkInstrumentErrors(dut) % function call to routine at end of program end voltage = zeros(1,4); for ch = eval(chanList) % for each channel in the channel list voltage(ch) = str2double(query(dut,['FETCh:VOLTage:OCV? (@' num2str(ch) ')'])); disp(voltage(ch)) if voltage(ch) > 4.2 || voltage(ch) < 2.5 error('abnormal cell voltage, abort') end end % Check for errors, HALT if any are found checkInstrumentErrors(dut) % function call to routine at end of program end % --------------------------------------------------------------- % INSITU % --------------------------------------------------------------- % Insitu Cal channels with cells detected for dut = BT2162B_Instruments % for each BT2162B fprintf(dut,['CALibration:WIRE:RESistance:INSitu (@' chanList ')']); end % --------------------------------------------------------------- % WAIT until all instruments are in 'wait for trigger' state % Check status operation condition 'wait for trigger' bit % bit 5 is the 6th bit (lsb), 1 = waiting for trigger, 0 = not waiting for dut = BT2162B_Instruments % for each BT2162B while 1 % Query the status operation condition register % Convert it to a binary number of at least 6 bits in length WaitForTrigger = dec2bin(str2double(query(dut,'STATus:OPERation:CONDition?')),6); % Check that bit 5 (6th bit) is a 1. % If so, move on to the next BT2162B. % If not, check again. if ( (str2double(WaitForTrigger(end-5)) == 1) ) % Bit 5 is 6th bit from end disp('correctly WAITING for a trigger') break % break out of while loop else % not yet waiting for trigger, must try again % can optionally insert a 1 second delay here. % Check for errors, HALT if any are found checkInstrumentErrors(dut) % function call to routine at end of program end end end
```

```
% --------------------------------------------------------------- % Send a TRIG command to the primary BT2162B only fprintf(dut1,'TRIGger'); % Note this communication is with dut1 only, not dut2 or dut3 % This will trigger the primary, and % cause pin 4 on the primary to output a trigger pulse. % This will go to all secondary pin 7's (trigger inputs) % and will trigger those instruments. % Also note that *TRG will not trigger unless source is 'BUS' % Here it is 'EXT', so TRIGger command is needed. % --------------------------------------------------------------- % WAIT for results for dut = BT2162B_Instruments % for each BT2162B while (1 ~= str2double(query(dut,'SENSe:WIRE:RESistance:AVAIlable?'))) % Check for errors, HALT if any are found checkInstrumentErrors(dut) % function call to routine at end of program end resistance = zeros(1,4); for ch = eval(chanList) % for each channel in the channel list resistance(ch) = str2double(query(dut,['CAL:WIRE:RES:VAL? (@' num2str(ch) ')'])); disp(resistance(ch)) if resistance(ch) > 5 || resistance(ch) < 0.001 error('abnormal pathh resistance, abort') end end % Check for errors, HALT if any are found checkInstrumentErrors(dut) % function call to routine at end of program fprintf(dut,'CALibration:WIRE:RESistance:SAVE 1'); end % --------------------------------------------------------------- % SDM % --------------------------------------------------------------- % Start SDM for dut = BT2162B_Instruments % for each BT2162B fprintf(dut,['INIT:TEST:MATC 60, 4.2, 2.8, 0.1, 10, -50e-6, 0.01, (@' chanList ')']); end % --------------------------------------------------------------- % WAIT until all instruments are in 'wait for trigger' state % Check status operation condition 'wait for trigger' bit % bit 5 is the 6th bit (lsb), 1 = waiting for trigger, 0 = not waiting for dut = BT2162B_Instruments % for each BT2162B while 1 % Query the status operation condition register % Convert it to a binary number of at least 6 bits in length WaitForTrigger = dec2bin(str2double(query(dut,'STATus:OPERation:CONDition?')),6); % Check that bit 5 (6th bit) is a 1. % If so, move on to the next BT2162B. % If not, check again. if ( (str2double(WaitForTrigger(end-5)) == 1) ) % Bit 5 is 6th bit from end disp('correctly WAITING for a trigger') break % break out of while loop else % not yet waiting for trigger, must try again % can optionally insert a 1 second delay here. % Check for errors, HALT if any are found checkInstrumentErrors(dut) % function call to routine at end of program
```

## 3 Operating the Analyzer

```
end end end % --------------------------------------------------------------- % Send a TRIG command to the primary BT2162B only fprintf(dut1,'TRIGger'); % Note this communication is with dut1 only, not dut2 or dut3 % This will trigger the primary, and % cause pin 4 on the primary to output a trigger pulse. % This will go to all secondary pin 7's (trigger inputs) % and will trigger those instruments. % Also note that *TRG will not trigger unless source is 'BUS' % Here it is 'EXT', so TRIGger command is needed. % --------------------------------------------------------------- % WAIT for SDM data to be available for dut = BT2162B_Instruments % for each BT2162B while 1 if ( str2double(query(dut,'FETC:CURR:LOG:POIN?')) < 1 ) % SDM data is not yet available, check again % Check for errors, HALT if any are found checkInstrumentErrors(dut) % function call to routine at end of program else % SDM data is available, check the next BT2162B break % break out of while loop end end end disp('SDM data is available on all instruments') % --------------------------------------------------------------- % End of program for dut = BT2162B_Instruments % for each BT2162B fprintf(dut,'*RST'); end return %function Fluca2_MultiFlucaSyncSQ_customerMethod_FW_1_12 % --------------------------------------------------------------- % checkInstrumentErrors routine function checkInstrumentErrors(dut) % This routine displays all errors in the error queue. % Then the routine errors if any errors exist. err_out = 0; while 1 val = query(dut, 'SYST:ERR?'); if strfind(val, 'No error') break else val err_out = 1; end end if err_out == 1 error('Instrument reported error(s)') end return % function checkInstrumentErrors(dut)
```

## Fault/ Inhibit System Protection

Asshown in the following figure, when the Fault outputs and Inhibit inputs of several instruments are daisy-chained, an internal fault condition in one of the units will disconnect all channels without intervention by either the controller or external circuitry. Note that when using the Fault/ Inhibit signals in this manner, both signals must be set to the same polarity.

Also, as shown in the figure, you can also connect the Inhibit input to a manual switch or external control signal that will short the Inhibit pin to common whenever it is necessary to disconnect all channels. Negative polarity must be programmed for all pins in this case. You can also use the Fault output to switch on an external relay circuit or signal other devices whenever a protection fault occurs.

![Image](%20BT2152B-prg_artifacts/image_000056_218e7e4e5eb0afe674f2414d459c36ca455380ba8c4ce92a4e59a41ed6dfc397.png)

## Clearing a System Protection Fault

To restore all instruments to a normal operating condition when a fault condition occurs in a daisychained system protection configuration, two fault conditions must be removed:

1. The initial protection fault or external Inhibit signal.
2. The subsequent daisy-chained fault signal (which is sourced by the Inhibit signal).

![Image](%20BT2152B-prg_artifacts/image_000057_327ee80b4217ea594ff6ade0f80449b57a5b49afc9623776a4f754eaf98f2abe.png)

Even when the initial fault condition or external signal is removed, the fault signal is still active and will continue to disconnect the channels of all the units.

To clear the daisy-chained fault signal if the operating mode of the Inhibit input is Live, simply clear the output protection on any ONEunit as explained under Clearing Protection Functions. If the operating modeof the Inhibit input is Latched, turn off the Inhibit input on ALL units individually. To re-enable the chain, re-program the Inhibit input on each unit to Latched mode.

## Using the Web Interface

Your Keysight BT2152A/B has a built-in Web interface that lets you control it directly from the Web browser on your computer. This is in addition to using the Interactive IOwithin the Connection Expert to communicate with your instrument as described in Connect the Interfaces, or writing a program to control the instrument.

With the Web interface, you can send SCPI commands directly to the instrument and also configure the LAN settings. Multiple simultaneous LAN connections are allowed.

NOTE

The built-in Web interface only operates over the LAN. A Web browser is required to use the Web Interface.

Step 1. Open the Web browser on your computer.

Step 2. Enter the instrument's hostname or IP address into the browser's Address field. .

You can obtain the IP Address from the Connection Expert Utility in the Keysight IOLibraries. In the IO Libraries My Instruments folder shown below, the IP address is located in the information box of the found (checked) instrument. It is also referenced in the VISA Address and SCPI Address information boxin the Details panel.

The Web interface is enabled when shipped. After the IP address is entered into the into the browser's Address field the following home page will appear:

![Image](%20BT2152B-prg_artifacts/image_000058_b6bd70b9d81311394bfc40b79234b2647cf2613b8353be552e81c27479399a46.png)

More Information

Tip: Check the Enable front panel identification indicator to cause the LAN status indicator on the front of the addressed unit to flash on and off to identify the unit being addressed.

Step 3. Click on the Control Instrument tab on the top of the page. Then click the Use Instrument IO button to begin controlling your instrument. This feature is the same as using the Interactive IOutility in the Keysight IOLibraries Suite.

![Image](%20BT2152B-prg_artifacts/image_000059_345f38f07b86a2982359f1566313589e9a2c53c92004e752d1b6200553dc864b.png)

Step 4. Click the Commands button and select IDN?(or type *IDN?) in the Command field. Click the Execute button. The Response history field shows the command sent and the reply, 'Keysight Technologies,BT2152A/B ,&lt;serial number&gt;,&lt;firmware revision codes&gt;' You can also enter and execute any other SCPI command into the Command field.

Step 5. Click the Configure LAN tab to configure the LAN settings. This page provides an overview of the current LAN settings and lets you change those settings. The initial page displays the current LAN configuration of your instrument. The Edit button opens the Edit Network Configuration page, which lets you set a unique host name and description. The Advanced options button accesses the reset network configuration option.

![Image](%20BT2152B-prg_artifacts/image_000060_45ea5bbf639d8ce3c5c8d9bf2281473eae2687493bfab930a5563928c2bc9b83.png)

![Image](%20BT2152B-prg_artifacts/image_000061_552c5f234e1a316be5b0a931e50999f9f9fc81e6da48b3ac35cfd6db385e1e6e.png)

For additional help about any of the pages, click on the ? button.

## Cell Testing Tips and Best Practices

ACell'sPercent State of Charge

Charge Redistribution and Equilibrium

Expected Self-Discharge Current and Temperature Dependency

Temperature Impact on Current Measurement

Impact of Stress and Vibration on Current Measurement

Noise Removal Functions

Optimizing Initial Current and Resistance Values

[NOTE](note.gif)

The voltage of most Lithium Ion cells is very sensitive to vibration and mechanical stress or deflection. Once a self-discharge test has started, the cell must not be moved or disturbed, and must not subjected to vibration. The temperature sensor must be mounted on or attached to the cell before the test and not be touched or have its connection adjusted during the test. Cells are microphonic - any touching, tapping, vibration, or shock will affect the cell's voltage and thus the measured current value.

## ACell'sPercent State of Charge

Self-discharge current is somewhat less for lower levels of percent state of charge (% SOC), falling off at a greater rate below ~45% SOC. The cell's voltage tends to be less stable and more temperature sensitive at lower levels of % SOC. For these reasons, it is generally recommended that the cells should ideally be at 60% SOC or higher for achieving good self-discharge current measurements.

## Charge Redistribution and Equilibrium

Right after a cell is charged or discharged, it takes a considerable amount of time for the electron charge to uniformly distribute itself within the cell and be at equilibrium. During this time, the cell's voltage is dropping or rising at an exponential rate, depending on whether it had been charged or discharged. In comparison, when a cell's charge is fully distributed and at equilibrium, its voltage falls off at a much lower and linear rate, due to the internal self-discharge current. Depending on the cell's makeup, it can take from several days to two weeks for a cell to reach charge equilibrium.

When the cell is connected to the Keysight BT2152A/B, the system holds its output voltage constant after the cell voltage matching process. If the cell is at charge equilibrium, the only influence on the cell's voltage is due to self-discharge. As the BT2152A/ B holds its voltage constant, the net result is the BT2152A/B needs to only replenish the self-discharge current to maintain constant voltage. However, when a cell has recently been charged or discharged and then connected to the BT2152A/B, additional charging current will be drawn from the BT2191A/B after charging, or discharging current in

## 3 Operating the Analyzer

addition to the self-discharge current will be sourced back into the BT2152A/B after discharging. The peak of this current can be several orders of magnitude greater than the self-discharge current alone.

## Expected Self-Discharge Current and Temperature Dependency

It is normal for cells to exhibit a small amount of self-discharge. It is difficult to definitively state what a cell's expected self-discharge current should be, as many factors exist regarding a cell's design and makeup that can affect this value. Notwithstanding, for cells at a room temperature of typically 23 °C, testing has shown it can typically range from just a few micro-amperes for sub 1 Ah cells to 50 to 100 micro-amperes for 10 to 20 Ah cells.

All other things being equal, a cell's self-discharge current can approximately double for a 10 °C increase in temperature. This applies to good cells not exhibiting excessive self-discharge leakage current caused by internal defects or other problems.

## Temperature Impact on Current Measurement

Acell's voltage temperature dependency can be expressed as a temperature coefficient of voltage (TCV), and can be quantified in microvolts per degree C ( μ V/ °C).Since the BT2152A/B'smethod to measure a cell's self-discharge current relies on matching its internal voltage source to the cell's voltage and then connecting them together, it is easy to see how the self-discharge current measurement is impacted by any change of the cell's voltage afterward. Several things can be done to reduce the effect of temperature on self-discharge current measurements:

- l It turns out a cell's TCV is dependent on its % SOC. It can vary from as low as zero at certain points to as much as hundreds of μ V/ °C,typically at very low % SOC levels. Generally having the cell charged to 70%SOCor better helps reduce the cell's TCV. Still, you may have to contend with a TCV in the range of 20 to 100 μ V/ °C
- l An indoor test environment can experience a few degrees temperature cycle each day. The series resistance between the BT2152A/B and the cell affects the measurement's sensitivity to the cell's TCV
- l Increasing this series resistance reduces the sensitivity to a cell's TCV but increases the time it takes for the measurement to settle to the final self-discharge current value.
- l The BT2152A/B has a programmable series resistance for this purpose.
- l Temperature sensitivity is a significant factor for larger cells, as they usually require a longer measurement settling time due to their proportionally larger capacity.
- l Depending on how long the self-discharge measurement takes, it may be necessary to take further steps to hold the cell's temperature steady. Possibilities include:
- l Surrounding the cell with thermal insulation.
- l Incorporating a substantial thermal mass (metal plate) that the cell is held against, to dampen temperature change. The thermal mass can be passive or actively temperature regulated.
- l Using a thermal chamber having a regulated temperature.

## Impact of Stress and Vibration on Current Measurement

Acell's voltage can be altered by mechanical stress and vibration. Any change of the cell's voltage impacts the self-discharge current. Static stress can induce a relatively fixed voltage shift while vibrations can create substantial peak-to-peak deviations in the measurement. Take care that you:

- l Do not subject the cell to stress.
- l isolate the cell from any direct vibration that may exist.

## Noise Removal Functions

In real world settings, self-discharge current measurement data shows significant noise, thereby complicating interpretation of the measurement results.

The primary source of measurement noise is temperature-induced cell open-circuit voltage changes, which translates into a noise component in the self-discharge current measurement. In the simplest case, there is one common noise source affecting all channels equally. In most cases however, the noise source may affect individual channels to a different degree and there may also be more than one noise source.

The Keysight BT2152A/B Self-Discharge Analyzer implements two noise removal functions: noise removal using median subtraction, and noise removal using median fitting. Refer to the FETCh:CURRent:MEDian commands.

Additional denoising utilities are available from Keysight. Contact your Keysight representative for moredetails. For further information on available noise-removal processing techniques please reference Application Note p/n 5992-3979EN Removing Noise in Lithium-Ion Battery Cell SelfDischarge Data Sets.

## Median Subtraction

The common noise source across channels can be extracted by comparing the individual channels and calculating the median signal at any given time, thereby canceling out the systematic variations of each curve and preserving the common noise. By subsequently subtracting the median from all signals eliminates the noise common to all channels, and centers the signals of the good curves around zero.

Median calculation assumes that majority of the cells in a measurement are good quality cells. If the bad cells approach 50% of the total, the median may start to fluctuate. Note that for median stability, it is important that a minimum number of at least eight channels are available for recording.

## Median Fitting

To preserve the overall shape of the original curve data, a fit of the median curve can be added back into the median subtraction result. This effectively discards any high-frequency variation in the median. The median fitting approach preserves most of the advantages of median subtraction, while making the curves more visually similar to the raw data.

## 3 Operating the Analyzer

Median calculation assumes that majority of the cells in a measurement are good quality cells. If the bad cells approach 50% of the total, the median may start to fluctuate. Note that for median stability, it is important that a minimum number of at least eight channels are available for recording.

## Optimizing the Initial Current and Resistance Settings

Finding the optimal values for initial current and output resistance can save measurement time without using excessively low output resistance (which is more susceptible to noise). This section provides a characterization procedure to help you choose the best values.

Usethe following procedure whenever you change to a new cell type that may have different characteristics (chemistry, construction, capacity, or package form-factor), or if something changes in the manufacturing process that changes the nominal self-discharge current. You don't necessarily have to repeat all steps for small changes in the above characteristics.

- l To minimize external temperature effects, perform this procedure using a stable thermal environment. It is critical to use and record the temperature as measured by the temperature sensor.
- l For the best representative results, always run the procedure with a statistically significant and representative sample from the population of cells to be tested.
- l The characterization procedure is an iterative process. For the most accurate results, you need to run all three tests: a 24-hour test, a 12-hour test, and a final 6-hour test. Additional time may be required for the cells to settle between tests. The additional time produces more accurate starting values.

Taking the time to complete this iterative process reduces the time you will need to spend on many successive tests, which can now be done using accurate (optimized) initial current and resistance values. This iterative process also minimizes the effects of all errors, including fluctuations caused by temperature variation.

## 24-hour test

Step 1. Set the initial current value for all cells to 0 A.

Step 2. Set the output resistance for all cells to a relatively high value. Low values are faster, but more susceptible to temperature variations and noise.

- l For the most accurate results, use an output resistance of 5 Ω or even higher. Using too low of a resistance makes your cells more sensitive to temperature variations and lead to wider variations in measurement. Using a higher resistance especially with large-capacity cells may require days for the test results to settle. The trade-off for a longer settling is that your results are less susceptible to noise or temperature variations. You will get very stable baseline measurements to determine the best Initial current value.
- l If you lack the time for a very long settling period, choose an output resistance appropriate for the cell size. You might start off with 5 Ω for a 2 Ah cell for example, or 0.5 Ω for a 20 Ah cell. The tradeoff will be a less accurate initial current value. Keep the start current at 0 A.

Step 3. Run the test for at least 24 hours or until the cells have obviously settled. The response plot should resemble an asymptotic curve and the cells should settle at about the same rate. Allow enough time to get a good average current.

Step 4. For the tested samples, note the average of the final settled current values (or the expected asymptotic resolution for the final values), omitting any results that are obviously outside the most tightly grouped results. Note this value as Limit(1).

## 12-hour test

- Step 1. Set the initial current value for all cells to the Limit(1) value you just noted.
- Step 2. Set the output resistance for all cells to a more moderate value (2.5 Ω if you started at 5 Ω for example).
- Step 3. Run the test again for at least 12 hours or until the cells have obviously settled.
- Step 4. Note the average of the final settled values (or the expected asymptotic resolution for the final values). Note this value as Limit(2).

## 6-hour test

- Step 1. Set the initial current value for all cells to the Limit(2) value you just noted.
- Step 2. Set the output resistance to your desired resistance (0.5 Ω for a 2 Ah cell for example). Keysight recommendsthat you set the resistance as high as possible to achieve your desired test results in the time allotted for testing. A quick test time at lower resistance is more susceptible to noise than a longer test time at higher resistance.
- l To determine when the cell reaches a stable value (meaning 3 R*C time constants or 95% as shown in the following graph), you will want to set the resistance (R) so that it achieves a final settled value within the time of the test. If the desired test time is 30 minutes for example, then you will need to set the Rsmall enough so that it reaches equilibrium within 30 minutes. The relationship between settling time and Ris linear as follows: Based on the 24 hour and 12 hour test - if it takes 10 hours to reach equilibrium at 5 Ω , it will reach equilibrium in 5 hours at 2.5 Ω , in 1 hour at 0.5 Ω , and in 30 minutes at 0.25 Ω .
- Step 4. Note the average of the final settled values (or the expected asymptotic resolution for the final values) and use this average as your optimized starting value for the initial microampere current value in subsequent testing.

Step 3. Run the test again with a test duration of at least 6 hours or until the cells have settled.

![Image](%20BT2152B-prg_artifacts/image_000062_9c7da5af7be8f1fc806b6d8bee84ae159202be51640abb734e14b7d8e2cfd043.png)

![Image](%20BT2152B-prg_artifacts/image_000063_b21ff9e84a8c9b3e139ab9e0a8d06f53b01311c76dadb725f580ce50e5dfa95e.png)

## 4 Programming Reference

Introduction to the SCPI Language

Programming Samples

CommandsbySubsystem

StatusTutorial

Reset and Interface Settings

SCPI Error Messages

## Introduction to the SCPI Language

CommandTypes

Keywords

Queries

Syntax Conventions

Parameter Types

Device Clear

## CommandTypes

SCPI (Standard Commands for Programmable Instruments) is an ASCII-based instrument command language designed for test and measurement instruments. SCPI has two types of commands, common and subsystem.

Commoncommands are defined by the IEEE488.2 standard to perform common interface functions such as reset, status, and synchronization. All common commands consist of a three-letter mnemonic preceded by an asterisk: *RST, *IDN?

Subsystemcommands perform specific instrument functions. They can be a single command or a group of commands. The groups are comprised of commands that extend one or more levels below the root. Subsystem commands are arranged alphabetically according to the function they perform. The following figure shows a portion of a subsystem command tree, from which you access the commands located along the various paths.

```
INITiate :TEST :OCV (@1)
```

## Keywords

Keywords, also referred to as headers, are instructions recognized by the instrument. Common commandsarealso keywords.

INITiate is the root keyword, TESTis a second-level keyword, OCV is a third-level keyword. Colons ( : ) separate the keyword levels.

The command syntax shows most commands (and some parameters) as a mixtureof upper- and lower-case letters. The upper-case letters indicate the abbreviated spelling for the command. For shorter program lines, you can send the abbreviated form. For better program readability, you can send the long form.

In the previous examples, INITand INITiate are both acceptable forms. You can use upper- or lowercase letters. Therefore, INITIATE, init, and Init are all acceptable.

## Queries

Following a keyword with a question mark ( ? ) turns it into a query (Example:

FETCh:CURRent:LATest?). If a query contains parameters, place the query indicator at the end of the

last keyword, before the parameters. Insert a space between the query indicator and the first parameter.

You can query the programmed value of most parameters. For example, you can query the latest current reading by sending:

```
FETCh:CURRent:LATest? (@1)
```

You must read back all the results of a query before sending another command to the instrument. Otherwise, a Query Interrupted error will occur and the unreturned data will be lost.

## Syntax Conventions

- l Colons ( : ) separate keyword levels. Blank spaces must be used to separate command parameters from their corresponding keyword. Note the space between VALue and the &lt;voltage&gt; parameter. If a command requires more than one parameter, use a comma to separate adjacent parameters. In the following calibration command, the voltage and current value parameters must be separated with a comma.
- l Triangle brackets ( &lt; &gt; ) indicate that you must specify a value for the enclosed parameter. In the example above, the &lt; voltage &gt; parameter is enclosed in triangle brackets. The brackets are not sent with the command string. You must specify a value for the parameter.
- l Avertical bar ( | ) separates multiple parameter choices for a given command string.
- l Square brackets ( [ ] ) enclose some syntax elements - nodes and parameters for example. This indicates that the element is optional and can be omitted. The bracketsare not sent with the command string. Any keyword enclosed in brackets is optional and can be omitted. However, if you are combining several commands within the same message string, you must include the optional commands to place the command parser at the correct level in the hierarchy.

```
CALibration:VALue <voltage>, <current>
```

## Parameter Types

The SCPI language defines several data formats to be used in commands and queries.

## Channel Parameter

The channel parameter &lt;chanlist&gt; is required to address one or more cell channels. Cell channels are numbered from 1 to 32. It has the following syntax for the entire range of channels:

## 4 Programming Reference

```
(@1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27 ,28,29,30,31,32) or (@1:32)
```

You can specify any combination of channels and ranges, provided the channels are in ascending order, as follows:

```
(@1:8,10,12,14,16,18,20:32)
```

The channel list, shown as &lt; chanlist &gt;throughout this document, must be preceded with the @symbol and must be enclosed in parentheses (). Query results are channel list order-sensitive. Results are returned in the order they are specified in the list.

![Image](%20BT2152B-prg_artifacts/image_000064_b98138907f5767063b2d231a2cd1344875f4d406f4284102e8aa7e20d10724a5.png)

When adding a channel list parameter to a query, you must include a space character between the query indicator (?) and the channel list parameter. Otherwise error -103, Invalid separator will occur.

## Numeric Parameters

Commandsthat require numeric parameters will accept all commonly used decimal representations of numbersincluding optional signs, decimal points, and scientific notation. If a command accepts only certain specific values, the instrument will automatically round the input numeric parameters to the accepted values. The following command requires a numeric parameter to enable channels 1 through 4 in the alarm register:

```
STATus:ALARm:ENABle 15
```

## Boolean Parameters

Boolean parameters represent a single binary condition that is either true or false. For a false condition, the instrument will accept "OFF" or "0". For a true condition, the instrument will accept "ON" or "1". When you query a Boolean setting, the instrument will always return "0" or "1". The following command requires a Boolean parameter:

```
SYSTem:COMMunicate:LAN:DHCP OFF|0|ON|1
```

## ASCII String Parameters

String parameters can contain virtually any set of ASCII characters. A string must begin and end with matching quotes; either a single quote or a double quote. You can include the quote delimiter as part of the string by typing it twice without any characters in between. The following uses a string parameter:

```
SYSTem:COMMunicate:LAN:DNS "198.105.232.4"
```

## Device Clear

Device Clear is an IEEE-488 protocol message that you can use to return the instrument to a responsive state. Different programming languages and IEEE-488 interface drivers provide access to this capability through their own unique commands. The status registers, the errorqueue, and all configuration states are left unchanged when a DeviceClear message is received.

Device Clear performs the following actions:

- l If a measurement is in progress, it is aborted.
- l The instrument returns to the trigger idle state.
- l The instrument's input and output buffers are cleared.
- l The instrument is prepared to accept a new command string.

NOTE

The ABORt command is the recommended method to terminate an instrument operation.

## 4 Programming Reference

## Programming Samples

Setting up and running a test

Retrieving all test values

Stopping/aborting a test

## Clearing protection events and errors

![Image](%20BT2152B-prg_artifacts/image_000065_b98138907f5767063b2d231a2cd1344875f4d406f4284102e8aa7e20d10724a5.png)

The unit requires a warm-up time of 1 hour for the measurement circuits to stabilize so that the test results meet specifications. When the unit is fully warmed up, the front panel Ready light changes from amber to green. You can send programming commands to the unit while it is warming up; you just cannot calibrate the unit.

## Setting up and running a test

You need only one command to set up and run a test. For example, send:

```
INITiate:TEST:MATChed 75, 4.2, 2.8, 1, 1, 0.0001, 0.001, (@1:16)
```

This command matches the cell open-circuit voltage at the start of the test and runs according to the following settings:

Test duration in minutes: 75

Maximum voltage: 4.2

Minimum voltage: 2.8

Output resistance in ohms: 1.0

Time interval in seconds: 1.0

Initial cell current in amps: 0.0001

Over-current protection in amps: 0.001

Cell channels: 1 through 16

The test begins immediately after sending this command.

The front panel Test light flashes blue when cell matching has been initiated. The light stops flashing and remains blue during the entire time the discharge test is running. After about 75 minutes, the test will stop, the Test light turns off, and the final discharge values are stored in the unit until the host computer reads the data out.

## INITiate:TEST:PROBecheck and query sequence

The following initiates a probe check test and returns the status of the channel probes.

```
INITiate:TEST:PROBecheck (@1:16) While(SENSe:PROBe:AVAIlable? == 0) \\ wait for data to become available Sleep(1000); FETCh:PROBecheck? (@1:16) \\ return comma-separated boolean values
```

## INITiate:TEST:OCV measurement and query sequence

The following initiates an open-circuit voltage test and returns the measured open-circuit voltage.

```
INITiate:TEST:OCV 4.2, 2.8, 0.001, 1, (@1:16) While(SENSe:OCV:AVAIlable? == 0) \\ wait for data to become available Sleep(1000); FETCh:VOLTage:OCV? (@1:16)
```

## INITiate:TEST:MATChed measurement and query sequence

The following matches the cell open-circuit voltage, initiates a test sequence, and returns the latest current and voltage measurement.

```
CALibration:WIRE:RESistance:INSitu (@1:16) INITiate:TEST:MATChed 75, 4.2, 2.8, 1, 0.125, 0.0001, 0.001, (@1:16) While(SENSe:TTIMe:REMaining? > 0) \\ wait for test to finish Sleep(1000); FETCh:VOLTage:LATest? (@1:16) FETCh:CURRent:LATest? (@1:16)
```

NOTE

Performing an in situ wiring resistance calibration immediately before the self-discharge measurement is recommended in order to obtain the best measurement results.

## Retrieving all test values

Onecommand returnsall test values from all specified cell channels. You can first query the number of available measurement points. Then retrieve the measurements.

```
FETCh:CURRent:LOG:POINts? \\ returns the number of available points FETCh:CURRent:LOG? 100, (@1:16)
```

This command retrieves 100 current measurements from channel 1 to 16. The readings are returned sequentially in channel groups (i.e. x,x,x,x,x,x,x,x, ... y,y,y,y,y,y,y,y, ...) where x represents all the measurementsfor channel 1, y represents all the measurements for channel 2 etc.

## Measurement array query and retrieval

The intent here is to query how many points are available, then use that information to query UP TO 200 but not more than the number of points available per channel. If the FETCh command is sent immediately after the INITiate:TESTcommand is sent, there may be no data to fetch for quite a while.

```
numCurrPointsPerChannel = 200; numCurrPointsPerChannel = min( numCurrPointsPerChannel , FETCh:CURRent:LOG:POINs? ) FETCh:CURRent:LOG? numCurrPointsPerChannel, (@1:16)
```

## Stopping/aborting a test

Because the INITiate:TESTcommands could take hours to execute, it may be necessary to stop the test in the middle to debug or fix a problem like a damaged fixture or cell installed backwards.

If the host computer is located in another building in a distributed factory environment, stopping the program may not be practical.

The front panel Stop button can be used to immediately stop a test. This will safely stop the test without losing test data or test configuration. Note that the ABORt command performs the same function as the front panel Stop button.

## Clearing protection events and errors

When the Error light is red, either a protection event or an error has occurred and need to be cleared.

Protection eventsoccur due to an over-voltage (OV), under-voltage (UV), or over current (OC) condition. The unit will latch off and cannot be operated until the fault is cleared. To clear the fault the cause of the fault must first be removed and then the protect status then needs to be cleared. These faults are part of the Alarm Status Group.

To query if a protection event has occurred, send:

```
STATus:ALARm:EVENt?
```

The value returned indicates the type of protection event: Over-voltage = 1; Over-current = 2; Undervoltage = 512. The command reads and clears the fault when it is sent to the instrument. To determine if the protection condition still exists, send:

```
STATus:ALARm:CONDition:CURRent? STATus:ALARm:CONDition:VOLTage? STATus:ALARm:CONDition:VOLTage:UNDer?
```

If a value other than zero is returned when these commands are sent, the condition is still present and must be removed. if the condition is no longer present, send the following command to clear protection status. This will turn the front panel Error light off.

```
OUTPut:PROTection:CLEar
```

Errorsoccur due to a variety of command processing errors, such as failing to read back the result from a query command. The instrument will continue to operate with errors present. Note that the front panel Error light does not turn on from command precessing errors.

To read and clear error codes send:

```
SYSTem:ERRor?
```

Each time this command is sent, one error is removed from the error queue. When the query returns a zero, all errors have been removed from the queue.

## CommandsbySubsystem

Calibration

CommonCommands

Configure

Digital

Fetch

Format

Initiate

LXI

Output

Sense

Status

System

## Calibration Commands

NOTE

Read the calibration section before calibrating. Improper calibration can reduce accuracy and reliability.

## CALibration:DATE&lt;" date "&gt; CALibration:DATE?

Stores the calibration date in nonvolatile memory. Enter any ASCII string up to 16 characters. The query returns the date. If no date is stored, an empty quoted string ("") is returned.

| Param eter                                                                   | TypicalReturn            |
|------------------------------------------------------------------------------|--------------------------|
| <"date">S tringprogramdata.E nclosestringparametersin singleor doublequotes. | dateof last calibra tion |
| Enter acalibrationdate:CAL:DAT E"2/2/2017"                                   |                          |

## CALibration:END

Endsthe calibration process. This command should be used after the calibration constants have been set, but before storing the calibration using the CALibration:STORe command.

| Param eter             | TypicalReturn   |
|------------------------|-----------------|
| (none)                 | (none)          |
| Endcalibration:CAL:END |                 |

## CALibration:LOAD

Loadsthe previous calibration values. For example, this can be used if there has been an error in the calibration procedure. This command is only valid prior to executing the CALibration:STORe command. OncetheCALibration:STORe command has been executed, the previous calibration values are overwritten.

| Param eter                                 | TypicalReturn   |
|--------------------------------------------|-----------------|
| (none)                                     | (none)          |
| Loadsthepreviouscalibrationvalues:CAL:LOAD |                 |

## CALibration:RESult? &lt; value &gt;

Used to enter the resulting measurement for calibration. The value entered depends on the calibration step. The command returns a zero (0) if the calibration step was successful.

| Param eter                                 |   TypicalReturn |
|--------------------------------------------|-----------------|
| <value>isthemeasuredresult                 |               0 |
| Enter acalibrationresult:CAL:R ES?1.234567 |                 |

- l If a value other than zero is returned, an error has occurred. Send SYSTem:ERRor? to return the error.

## CALibration:SECure:CODE&lt; code &gt;

Sets the security code to prevent unauthorized calibration.

| Param eter                                      | TypicalReturn   |
|-------------------------------------------------|-----------------|
| <code>integer from1to10E 32                     | (none)          |
| Enter acalibrationcode:CAL:SE C:C ODE1223334444 |                 |

- l Once set, you must unsecure the unit to calibrate it, or change the calibration string or security code.
- l When shipped from the factory the instrument is unsecured, with the security code set to 0 (zero).
- l You cannot update the firmware using the Keysight utility without the code if calibration is locked.

## CALibration:SECure:STATe 0|OFF|1|ON ,&lt; code &gt; CALibration:SECure:STATe?

| Param eter                            | TypicalReturn   |
|---------------------------------------|-----------------|
| 0&#124;O FF&#124;1&#124;ON            | 0 or 1          |
| <code>0,or aninteger from1to10E 32    | 0               |
| Enablethesecurecode:C AL:SEC:STATON,0 |                 |

## CALibration:STARt

Initiates the calibration procedure. The command does the following:

- l Sends a *RSTcommand
- l Closes the output relays on all channels
- l Disables the OVP, UVP, OCP, and UCPprotections
- l Sets all instrument DACs to 3.5 V.
- l Sets the calibration status bit

| Param eter                 | TypicalReturn   |
|----------------------------|-----------------|
| (none)                     | (none)          |
| Start calibration:CAL:STAR |                 |

## CALibration:STEP &lt; step &gt; CALibration:STEP?

Steps through the reference calibration process; executes a reset after the command is sent. The query returns 0 (zero) if no step is sent. Step 1 calibrates the voltage; step 2 calibrates the voltage offset; step 3 calibrates the 10 mA current.

| Param eter                        | TypicalReturn   |
|-----------------------------------|-----------------|
| <step>number from1-3              | 0-3             |
| Executecalibrationstep1:CAL:STEP1 |                 |

## CALibration:STORe

Stores the calibration constants in the EEPROM. This step overwrites the previous calibration constants. This command should be used after calibration has ended using CALibration:END.

| Param eter                            | TypicalReturn   |
|---------------------------------------|-----------------|
| (none)                                | (none)          |
| Storethecalibrationconstants:CAL:STOR |                 |

## CALibration:STRing &lt;" string "&gt; CALibration:STRing?

Stores a message in calibration memory. Common messages include the last calibration date, calibration due date, or calibration contact information. You can perform this query regardless of whether the instrument is secured.

| Param eter                                                              | TypicalReturn                                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Quotedstringof upto128characters                                        | "Default Calibration"                                                   |
| Tostoreacal string:CAL:ST R:"C alibrationmust beperformedinthecal lab." | Tostoreacal string:CAL:ST R:"C alibrationmust beperformedinthecal lab." |

## CALibration:VALue? &lt; step &gt;

Returns the reference calibration constants of the specified step. Values are either in volts or amps, depending on the step. This allows you to query the reference calibration values before doing a new calibration to see how far the references have shifted.

| Param eter                                         | TypicalReturn               |
|----------------------------------------------------|-----------------------------|
| <step>number from1- 3                              | calibrationconstant (Vor I) |
| Returnsthecalibrationconstant for step1:C AL:VAL?1 |                             |

## CALibration:VERification:END

Endsthe verification process. This command should be used after the SENSe:VERification:AVAIlable command returns a one (1) to indicate that the calibration verification has completed.

| Param eter                           | TypicalReturn   |
|--------------------------------------|-----------------|
| (none)                               | (none)          |
| Endchannel verification:CAL:VE R:END |                 |

- l If an ABORt, *RST or device clear command is sent while verification is in progress, all channel settings will revert to their default settings.

## CALibration:VERification:MEASure:INITiate &lt; time &gt;, &lt; tint &gt;

Initiates a measurement with the specified input parameters. The front panel Test light flashes orange when this command is executed.

| Param eter                                                             |   TypicalReturn |
|------------------------------------------------------------------------|-----------------|
| <time>verificationdurationinseconds                                    |               1 |
| <tint>betweensamplesinseconds,from1to250                               |               1 |
| Set thetimelimit andtimeinterval for verification:CAL:ME AS:T INT10,10 |                 |

- l The results can be returned with the FETCh commands (i.e. FETCh:VOLTage:LATest?, FETCh:CURRent:LOG?).

## CALibration:VERification:STARt &lt; channel &gt;

Initiates the channel verification procedure on the specified channel.

| Param eter                                | TypicalReturn   |
|-------------------------------------------|-----------------|
| <channel>thechannel toverify:from1- 32 1  |                 |
| Start channel verification:CAL:VE R:STAR1 |                 |

## CALibration:VERification:VOLTage &lt; voltage &gt; CALibration:VERification:VOLTage?

Used to enter the voltage limit for verification. All channels included in channel verification will be set to this limit.

| Param eter                                                      | TypicalReturn   |
|-----------------------------------------------------------------|-----------------|
| <voltage>thevoltagelimit for theactivechannels                  | <voltage>       |
| Set thevoltagelimit for channel verification:CAL:VE R:VO LT4.5) | <voltage>       |

- l An error is returned if the channel voltage exceeds the voltage limit.

## CALibration:WIRE:RESistance:AUTO CALibration:WIRE:RESistance:BYSHort

These commandsare synonymous. They run cable resistance calibration on all channels with the ends of the cell cables shorted. The commands take about 20 minutes. Refer to By-short Calibration.

IMPORTANT Disconnect all cells from the cables. Short the ends of the cell cables together. NOTE

| Param eter                                                        | TypicalReturn   |
|-------------------------------------------------------------------|-----------------|
| (none)                                                            | (none)          |
| Start wireresistancecalibration:CAL:WIR E:R ES:AUTOor CAL:WIR E:R | ES:BY SH        |

- l Wire resistance values can be retrieved using SENSe:WIRE:RESistance:CONFigure? query.
- l Use CALibration:WIRE:RESistance:SAVEto place the values in non-volatile memory.
- l The procedure flashes the Test light orange and sets the calibration bit while running.

## CALibration:WIRE:RESistance:CLEar

Resets all the volatile wiring resistance values to 0 (zero). You must load a wire resistance file or run wire-resistance calibration in order to use non-zero resistance values.

| Param eter                                                        | TypicalReturn   |
|-------------------------------------------------------------------|-----------------|
| (none)                                                            | (none)          |
| Resetsthewireresistancecalibrationvaluestozero:CAL:WIR E:R ES:CLE |                 |

- l Turning power on will also reset all wiring resistance values to zero.
- l Values saved to non-volatile memory are not cleared.

## CALibration:WIRE:RESistance:INSitu (@&lt;chanlist&gt;)

Runscalibration of the cable resistance on the specified channels with the battery cells connected (in situ). This command takes about 2 minutes or so. You may specify the expected current on the battery cells using the CONFigure:INSitu:CURRent command. Refer to In situ Calibration.

IMPORTANT The LI cells must be connected to the specified channels for in situ calibration. NOTE

| Param eter                                                                             | TypicalReturn   |
|----------------------------------------------------------------------------------------|-----------------|
| <chanlist>activechannelsfrom1- 4.                                                      | (none)          |
| Startstheinsituwireresistancecalibrationonthespecifiedchannels:CAL:WIR E:R ES:INS(@1:4 |                 |

- l Wire resistance values can be retrieved using CALibration:WIRE:RESistance:VALues?.
- l Use CALibration:WIRE:RESistance:SAVEto place the values in non-volatile memory.

- l The procedure flashes the Test light orange and sets the calibration bit while running.
- l Performing an in situ wiring resistance calibration immediately before the self-discharge measurement is recommended in order to obtain the best measurement results.

## CALibration:WIRE:RESistance:LOAD &lt;value&gt;

Loadsthe wire resistance values from the specified file location.

| Param eter                                                   | TypicalReturn   |
|--------------------------------------------------------------|-----------------|
| <value>resistancefilenamefrom1- 5                            | (none)          |
| Loadsthewireresistancevaluesinlocation1:CAL:WIR E:R ES:LOAD1 |                 |

- l To use the wire resistances from a loaded resistance file, a subsequent INITiate:TEST:MATChed command must be performed.

## CALibration:WIRE:RESistance:VALues&lt; resistance &gt;, (@&lt;chanlist&gt;) CALibration:WIRE:RESistance:VALues? (@&lt;chanlist&gt;)

This command is synonymous with SENSe:WIRE:RESistance:CONFigure. It sets the wiring resistance of the specified channels. The query returns the presently set wiring resistance of the specified channels. Refer to Wire Resistance Calibration for more information.

| Param eter                                                                                 | TypicalReturn   |
|--------------------------------------------------------------------------------------------|-----------------|
| <resistance>theresistanceof thewireinohms,from0 Ω to5 Ω ; res- olution:0.001 Ω ; Default:0 | 0               |
| <chanlist>activechannelsfrom1- 4                                                           | (none)          |
| Specifiesawireresistanceof 0.188 Ω for channel 1:CAL:WIR E:R ES:VAL0.188,(@1)              |                 |

![Image](%20BT2152B-prg_artifacts/image_000066_8eb5bebdf8e2740a8c7d1d88cdc570ab65971eaf14218a1041e98537227e5068.png)

Wire resistance calibration is required when all cell connectors have been installed in the instrument and whenever any cell connector is unplugged, reinserted, or reseated.

## CALibration:WIRE:RESistance:SAVE&lt;value&gt;

Saves the wire resistance values to the specified file location in non-volatile memory.

| Param eter                                                  | TypicalReturn   |
|-------------------------------------------------------------|-----------------|
| <value>resistancefilenamefrom1- 5                           | (none)          |
| Savethewireresistancevaluesinlocation1:CAL:WIR E:R ES:SAVE1 |                 |

- l This includes any changed values from the SENSe:WIRE:RESistance:CONFigure command.
- l To use the wire resistances after having performed the wire resistance calibration, a subsequent INITiate:TEST:MATChed command must be performed.

## CommonCommands

## ABORt

Aborts a measurement in progress, returning the instrument to the trigger idle state.

| Param eter                           | TypicalReturn   |
|--------------------------------------|-----------------|
| (none)                               | (none)          |
| Abort themeasurement inprogress:ABOR |                 |

## *CAL?

Transfers the calibration values to the instrument channels. This calibration is automatic and can take up to 1 hour for the BT2152A/B. Returns a 0 (zero) when successful, and an error code otherwise.

![Image](%20BT2152B-prg_artifacts/image_000067_2d1e5962d79cfda0438d80518dd9317f69a580a478699925a614623fe064289d.png)

IMPORTANT Remove all connections from the CAL connector on the rear panel of the BT2152A/B before performing the channel calibration.

| Param eter   |   TypicalReturn |
|--------------|-----------------|
| (none)       |               0 |

Initia tetra ns fe r of ca libra tion v a lue s to cha nne ls : *C A L ?

- l The unit must pass self-test, which is run at the start of channel calibration. If self-test (*TST?) does not pass, channel calibration will abort.
- l The unit must be warmed up. A warm up time of 1 hour is required before the unit can be calibrated. The Ready light must be green, otherwise *CAL? will abort.
- l If channel calibration fails, an error will be placed in the error queue with the channel number that failed along with measurement information detailing the issue. Use SYSTem:ERRor? to read the error queue. See SCPI Error Messages for more information.
- l Sets the calibration status bit.

## *CLS

Clear Status Command . Clears the event registers in all register groups. Also clears the Status Byte and Error Queue. If *CLS immediately follows a program message terminator (&lt;NL&gt;), then the Output Queueand the MAVbit are also cleared. Refer to Status Tutorial for more information.

| Param eter                                                | TypicalReturn   |
|-----------------------------------------------------------|-----------------|
| (none)                                                    | (none)          |
| Clear Event register bits,Statusbyte,andE rror queue:*CLS |                 |

## *ESE &lt;mask&gt;

Standard Event Status Enable . Enables one or more events in the Standard Event Status Register to be reported in bit 5 (the Standard Event Status Summary Bit) of the Status Byte Register. You enable an event by specifying its decimal weight for &lt;mask&gt; . To enable more than one event, specify the sum of the decimal weights.

| Param eter                                                       | TypicalReturn                           |
|------------------------------------------------------------------|-----------------------------------------|
| <mask>                                                           | (none)                                  |
| Sumofdecimal weightsof StatusR egister bits.SeeStatus bits4and2. | Byte Register.For example, *E SE20 sets |

## *ESE?

Standard Event Status Enable Query . Returns the weighted sum of all enabled (unmasked) bits in the Standard Event Status Register.

| Param eter                                     | TypicalReturn                                                                |
|------------------------------------------------|------------------------------------------------------------------------------|
| (none)                                         | <Weightedsumof all enabled(unmasked)bitsintheStandardE vent StatusR egister> |
| ReturntheStandardE vent StatusR egister:*E SE? |                                                                              |

## *ESR?

Standard Event Status Register Query . Returns the weighted sum of all set bits in the Standard Event Status Register. After reading the register, *ESR?clears the register. The events recorded in the Standard Event Register are independent of whether or not those events are enabled with the *ESE command.

| Param eter                                     | TypicalReturn                                                   |
|------------------------------------------------|-----------------------------------------------------------------|
| (none)                                         | <Weightedsumof all set (unmasked)bitsintheStandardE vent Status |
|                                                | Register>                                                       |
| ReturntheStandardE vent StatusR egister:*E SR? |                                                                 |

## *IDN?

Identification Query . Returns instrument's identification string, which contains four comma-separated fields. The first field is the manufacturer's name, the second field is the instrument model number, the third field is the serial number, and the fourth field is the firmware revision.

| Param eter                                      | TypicalReturn                                   |
|-------------------------------------------------|-------------------------------------------------|
| (none)                                          | <ASCII stringwithcomma-separatedfields>         |
| Returntheinstrument'sidentificationstring:*IDN? | Returntheinstrument'sidentificationstring:*IDN? |

## 4 Programming Reference

- l Response format: Keysight Technologies,BTxxxxB,&lt;serial number&gt;,&lt;revision codes&gt;
- l Typical return: Keysight Technologies,BT2152B,MY06009010,A.01.51-60-04-10 where:

A.01 = major firmware revision

- .51 = minor firmware revision
- -60 = primary FPGA revision
- -04 = secondary FPGA revision
- -10 = mainboard ID

## *OPC?

The command sets bit 0 in the Standard Event Register when operation completes. The response is delayed until all pending operations such as the INIT:TESTor calibration commands complete.

| Param eter                          |   TypicalReturn |
|-------------------------------------|-----------------|
| (none)                              |               1 |
| Returna1whencommandscomplete:*O PC? |                 |

- l The purpose of this command is to synchronize your application with the instrument.
- l Other commands cannot be executed until this command completes.

## *RST

Reset Command Resets the instrument to pre-defined values that are either typical or safe. These settings are described under Reset State.

| Param eter               | TypicalReturn   |
|--------------------------|-----------------|
| (none)                   | (none)          |
| Reset theinstrument:*RST |                 |

- l *RSTno longer affects the DIGITAL:PINx:POLarity values. This avoids transitions on the DIOpins during calibration.
- l DIGITAL: PIN:FUNCtion is not affected.
- l *RSTforces the ABORt command. This cancels any measurement actions presently occurring.
- l Allow at least 4 seconds for the *RST to complete. Set the IO timeout to &gt;4 seconds.

## *SRE &lt;mask&gt;

Service Request Enable When a service request event occurs, it sets a corresponding bit in the Status Byte Register (this happens whether or not the event has been enabled (unmasked) by *SRE). The *SRE command allowsyou to identify which of these events will assert a service request (SRQ). When an event is enabled by *SREand that event occurs, it sets a bit in the Status Byte Register and issues an SRQto the computer (sets the GPIB SRQline true). You enable an event by specifying its decimal weight for &lt;mask&gt;. To enable more than one event, specify the sum of the decimal weights.

| Param eter                                         | TypicalReturn                  |
|----------------------------------------------------|--------------------------------|
| (none)                                             | (none)                         |
| ServiceR equest Enable:*SRE192.E nablesbits6and7.R | espectiveweightsare64+128=192. |

## *STB?

Status byte query. Reads the Status Byte Register, which contains the status summary bits and the Output Queue MAVbit. The Status Byte is a read-only register and the bits are not cleared when it is read. Refer to Status Tutorial for more information.

| Param eter           | TypicalReturn   |
|----------------------|-----------------|
| (none)               | <bit value>     |
| Readstatusbyte:*STB? |                 |

## *TST?

SelfTest Query . Performs an instrument self-test. A 0 (zero) indicates the instrument passed self-test. If self-test fails, one or more error messages will provide additional information. Use SYSTem:ERRor? to read the error queue. See SCPI Error Messages for more information.

| Param eter              | TypicalReturn   |
|-------------------------|-----------------|
| (none)                  | 0or1            |
| Performself-test:*T ST? |                 |

## *WAI

Pauses additional command processing until all pending operations such as the INIT:TESTcommands are complete. See OPCfor more information.

| Param eter                                    | TypicalReturn   |
|-----------------------------------------------|-----------------|
| (none)                                        | (none)          |
| Wait until all pendingoperationscomplete.*WAI |                 |

- l *WAI can only be aborted by sending the instrument a Device Clear command.

## CONFigure Command

## CONFigure:INSitu:CURRent HIGH|MED|LOW CONFigure:INSitu:CURRent?

Configures the current used during the in situ wire resistance calibration.

HIGH - specifies ±9 mA

MED - specifies ±5 mA

LOW - specifies ±1 mA

| Param eter                                     | TypicalReturn   |
|------------------------------------------------|-----------------|
| HIG H&#124;MED&#124;LOW,                       | LOW             |
| *RSTLOW                                        |                 |
| Toset themediuminsitucurrent:C ONF:INS:CURRMED |                 |

## CONFigure:TEST:WIRE:RESistance 5 | 10 | 20 |&lt; value &gt; CONFigure:TEST:WIRE:RESistance?

Selects the wiring resistance range to use on all channels.

Value can be any number between 0 and 20. If the &lt; value &gt;input to the command is ≤ 5, then the 5 Ω range is selected (default range). If the &lt; value &gt;input is &gt;5 but ≤ 10, then the 10 Ω range is selected. If the &lt; value &gt;input is &gt;10 but ≤ 20 then the 20 Ω range is selected.

- 5 Ω is default range.
- Resettable by *RST.

The wiring resistance range is used by the in situ wiring resistance Calibration and the self-discharge test.

Approximate time required for in situ wiring resistance Calibration to complete:

| 5 Ω range   | 10 Ω range   | 20 Ω range   |
|-------------|--------------|--------------|
| 90seconds   | 170seconds   | 250seconds   |

Approximate time required for the self-discharge test to start:

| 5 Ω range   | 10 Ω range   | 20 Ω range   |
|-------------|--------------|--------------|
| 110seconds  | 230seconds   | 350seconds   |

Typical return, one of three range values: 5, 10, or 20.

## Digital Commands

Digital commands program the digital control port on the rear panel of the instrument. The [SOURce:] keyword is optional.

## [SOURce:]DIGital:INPut:DATA?

Readsthe state of the digital control port. Returns the binary-weighted value of the state of pins 1 through 7 in bits 0 through 6 respectively.

| Param eter                                             | TypicalReturn   |
|--------------------------------------------------------|-----------------|
| (none)                                                 | <bit value>     |
| Readsthestateof thedigital control port:DIG :INP:DATA? |                 |

## [SOURce:]DIGital:OUTPut:DATA&lt; value &gt; [SOURce:]DIGital:OUTPut:DATA?

Sets the state of the digital control port. This only affects the pins whose function has been set to Digital IO operation. The port has seven signal pins and a digital ground pin. In the binary-weighted value that is written to the port, the pins are controlled according to the following bit assignments:

| Pin             |   1 |   2 |   3 |   4 5 |   6 |   7 |
|-----------------|-----|-----|-----|-------|-----|-----|
| Bit number 0    |   1 |   2 |   3 |     4 |   5 |   6 |
| Decimal value 1 |   2 |   4 |   8 |    16 |  32 |  64 |

Bit values corresponding to digital port pins that are not configured as DIOare ignored.

| Param eter                              | TypicalReturn   |
|-----------------------------------------|-----------------|
| 0-127,                                  | <bit value>     |
| *RST0                                   | <bit value>     |
| Programspins1,3,and5on:DIG :O UTP:DATA? | <bit value>     |

## [SOURce:]DIGital:PIN&lt;1-7&gt;:FUNCtion &lt; function &gt; [SOURce:]DIGital:PIN&lt;1-7&gt;:FUNCtion?

Sets the digital pin function. Refer to Understanding the Digital Port for further information.

DIO

DINPut Digital input/output mode Digital input-only mode.

FAULt Pin 1 functions as an isolated fault output. Pin 2 is common for pin 1

INHibit Pin 3 functions as an inhibit input.

## 4 Programming Reference

| Param eter                                           | TypicalReturn      |
|------------------------------------------------------|--------------------|
| DIO&#124;DINPut &#124;FAULt &#124;INHibit *RSTDINPut | DIO ,DINP,FAUL,INH |
| Setspin1toFAULt mode:DIG :PIN1:FUNCFAUL              |                    |

## [SOURce:]DIGital:PIN&lt;1-7&gt;:POLarity POSitive|NEGative [SOURce:]DIGital:PIN&lt;1-7&gt;:POLarity?

Sets the pin polarity. POSitive meansalogical true signal is a voltage high at the pin. NEGative means a logical true signal is a voltage low at the pin.

| Param eter                                   | TypicalReturn   |
|----------------------------------------------|-----------------|
| POSitive&#124;NE Gative, *RSTPO Sitive       | POSorNEG        |
| Setspin1toPO Sitivepolarity:DIG :PIN1:POLPOS |                 |

## Fetch Commands

Fetch commandsreturn measurement data that has been acquired once a test has been started using the INITiate:TESTcommands. They also return measurement data from an external thermistor connected to the rear panel TEMPinput.

FETCh:CURRent:LATest?(@&lt;chanlist&gt;)

FETCh:VOLTage:LATest?(@&lt;chanlist&gt;)

Returns the most recent measurement for the specified channels in ASCII.

| Param eter                                                                    | TypicalReturn                              |
|-------------------------------------------------------------------------------|--------------------------------------------|
| (none)                                                                        | Comma-separatedvaluesfromspecifiedchannels |
| <chanlist>activechannelsfrom1- 32                                             | (none)                                     |
| Returnsthelatest current measurement for thespecifiedchannels:FE TC:C URR:LAT | ?(@1:4)                                    |
| Returnsthelatest voltagemeasurement for thespecifiedchannels:FE TC:V OLT:LA   | T?(@1:4)                                   |

- l The FETCh? query does not erase measurements from the reading memory. You can send the query multiple times to retrieve the same data. 8192 is the maximum number of ASCII values that can be returned in any one call.
- l The instrument clears all measurements from reading memory whenever INITis executed.
- l If INITiate:TEST:MATChed has been configured for a different channel group than the channel group specified in this command, non-active channels will return +9.91000000e37 (Not-A-Number).

FETCh:CURRent:LOG?&lt; values/ chan &gt; [,&lt; offset/ chan &gt;], (@&lt;chanlist&gt;)

```
FETCh:VOLTage:LOG?< values/ chan > [,< offset/ chan >], (@<chanlist>)
```

Returns the current or voltage measurement log for the specified channels in ASCII.

| Param eter                                                                                                              | TypicalReturn                                      |
|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <values/chan>number of readingsreturnedper channel                                                                      | Multiplecomma-separatedvaluesfromspecifiedchannels |
| <offset/chan>optional valuethat offsetsor skipsthenum- ber of readingsreturnedfromthebeginningof thedatalog             | (none)                                             |
| <chanlist>activechannelsfrom1- 32                                                                                       | (none)                                             |
| Returns10current readingsper specifiedchannel:FE TC:C URR:LO Returns10voltagereadingsper specifiedchannel:FE TC:VOLT:LO | G?10,(@1:4) G?10,(@1:4)                            |

- l The readings are returned sequentially in channel groups (i.e. x,x,x,x,x,x,x,x, y,y,y,y,y,y,y,y, … .) Where x represents all measurements for channel 1, y represents all measurements for channel 2 etc.
- l The &lt;values/chan&gt; parameter specifies the number of readings. So, for example, if (@1:4) is the specified channel list and values/ chan is specified as 10, a total of 40 values will be returned.
- l If an &lt;offset/ chan&gt; value of 5 is specified, the first 5 readings in each channel log are not returned.

## 4 Programming Reference

- l The FETCh? query does not erase measurements from the reading memory. You can send the query multiple times to retrieve the same data. 8192 is the maximum number of ASCII values that can be returned in any one call.
- l Use FETCh:CURRent:LOG:POINts? or FETCh:VOLTage:LOG:POINts? to query how many measurement values (points) are available.
- l The instrument clears all measurements from reading memory whenever INITis executed.
- l If INITiate:TEST:MATChed has been configured for a different channel group than the channel group specified in this command, non-active channels will return +9.91000000e37 (Not-A-Number).

## FETCh:CURRent:LOG:BINary?&lt; values/ chan &gt; (@&lt;chanlist&gt;) FETCh:VOLTage:LOG:BINary?&lt; values/ chan &gt; (@&lt;chanlist&gt;)

Returns the current or voltage measurement log for the specified channels in binary. These commands allow you to return all the data instead of being limited to 8192 values like ASCII readings. Use the FORMat:BORDer command to format the binary data.

| Param eter                                                                                                                                | TypicalReturn                   |
|-------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| <values/chan>number of readingsreturnedper channel                                                                                        | <binarydatastring>              |
| <chanlist>activechannelsfrom1- 32                                                                                                         | (none)                          |
| Returns10current readingsper specifiedchannel inbinary:FE TC:C URR:LO Returns10voltagereadingsper specifiedchannel inbinary:FE TC:VOLT:LO | G:BIN?10,(@1:4) G:BIN?10,(@1:4) |

- l The readings are returned sequentially in channel groups (i.e. xxxxxxxxyyyyyyyy … .) Where x represents all measurements for channel 1, y represents all measurements for channel 2 etc. Each data point takes up 64 bits. The values returned are 64-bit floating point numbers.
- l The &lt;values/chan&gt; parameter specifies the number of readings. So, for example, if (@1:4) is the specified channel list and values/ chan is specified as 10, a total of 40 values will be returned.
- l The FETCh? query does not erase measurements from the reading memory. You can send the query multiple times to retrieve the same data.
- l Use FETCh:CURRent:LOG:POINts? or FETCh:VOLTage:LOG:POINts? to query how many measurement points are available.
- l The instrument clears all measurements from reading memory whenever INITis executed.
- l If INITiate:TEST:MATChed has been configured for a different channel group than the channel group specified in this command, non-active channels will return +9.91000000e37 (Not-A-Number).

## FETCh:CURRent:LOG:POINts? FETCh:VOLTage:LOG:POINts?

Returns the number of readings available per channel of the active channels specified in the INIT command.

| Param eter                                                                                                                                |   TypicalReturn |
|-------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| (none)                                                                                                                                    |            4020 |
| Returnsthenumber of current readingsavailable:FE TC:C URR:LO G:PO IN? Returnsthenumber of voltagereadingsavailable:FE TC:VOLT:LO G:PO IN? |                 |

- l If you attempt to return more readings than are available, an error will be generated. You must include any offset/ chan values in the total number of readings available.

## FETCh:CURRent:MEDian:FIT:LOG?&lt; values/ chan &gt; [,&lt; offset/ chan &gt;], (@&lt;chanlist&gt;) FETCh:CURRent:MEDian:SUBtraction:LOG?&lt; values/ chan &gt; [,&lt; offset/ chan &gt;], (@&lt;chanlist&gt;)

These queries remove unwanted noise from the self-discharge measurements. Refer to Noise Removal Functions for further information.

The median subtraction query returns the processed measurement results. The processing algorithm takes the median of every measurement in the channel list for each point in time and subtracts that median from every measurement point. The resulting data points are then returned.

The median fit query returns further processed measurement results from the median subtraction query. This algorithm first performs median subtraction processing. An exponential fit to the median vector which was subtracted is then added back into the data points, which are then returned.

The processing algorithms can only analyze 3,600 measurement points. This is equivalent to 1 hour's worth of measurements at 1-second intervals. Measurements above the 3,600 limit will be ignored and an error will be generated.

| Param eter                                                                                                                                                          | TypicalReturn                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <values/chan>number of readingsreturnedper channel                                                                                                                  | Multiplecomma-separated valuesfromspecifiedchannels |
| <offset/chan>optional valuethat offsetsor skipsthenum- ber of readingsreturnedfromthebeginningof thedatalog                                                         | (none)                                              |
| <chanlist>activechannelsfrom1- 4                                                                                                                                    | (none)                                              |
| Returns10mediansubtractionreadingsper specifiedchannel:FE TC:CURR:ME D:SUBT :LO Returns10medianfit readingsper specifiedchannel:FE TC:CURR:ME D:FIT :LO G?10,(@1:4) | G?10,(@1:4)                                         |

- l Both of these queries must have at least two channels in the chanlist, or an error will be generated.
- l The readings are returned sequentially in channel groups (i.e. x,x,x,x,x,x,x,x, y,y,y,y,y,y,y,y, … .) Where x represents all measurements for channel 1, y represents all measurements for channel 2 etc.

## 4 Programming Reference

- l The &lt;values/chan&gt; parameter specifies the number of readings. So, for example, if (@1:4) is the specified channel list and values/ chan is specified as 10, a total of 40 values will be returned.
- l If an &lt;offset/ chan&gt; value of 5 is specified, the first 5 readings in each channel log are not returned.
- l The FETCh? query does not erase measurements from the reading memory. You can send the query multiple times to retrieve the same data.
- l Use FETCh:CURRent:MEDian:SUBtraction:LOG:POINts? or FETCh:CURRent:MEDian:FIT:LOG:POINts? to query how many measurement values (points) are available.
- l The instrument clears all measurements from reading memory whenever INITis executed.
- l If INITiate:TEST:MATChed has been configured for a different channel group than the channel group specified in this command, non-active channels will return +9.91000000e37 (Not-A-Number).

## FETCh:CURRent:MEDian:FIT:LOG:BINary? &lt; values/ chan &gt;, (@&lt;chanlist&gt;) FETCh:CURRent:MEDian:SUBtraction:LOG:BINary? &lt; values/ chan &gt;, (@&lt;chanlist&gt;)

Returns the processing algorithm values for the specified channels in binary.

The processing algorithms can only analyze 3,600 measurement points. This is equivalent to 1 hour's worth of measurements at 1-second intervals. Measurements above the 3,600 limit will be ignored and an error will be generated.

| Param eter                                                         | TypicalReturn                                                     |
|--------------------------------------------------------------------|-------------------------------------------------------------------|
| <values/chan>number of readingsreturnedper channel                 | <binarydatastring>                                                |
| <chanlist>activechannelsfrom1- 4                                   | (none)                                                            |
| Returns10mediansubtractionreadingsper specifiedchannel inbinary:FE | TC:CURR:ME D:SUBT :LO G:BIN?10,(@1:4)                             |
| Returns10medianfit readingsper                                     | specifiedchannel inbinary:FE TC:CURR:ME D:FIT :LO G:BIN?10,(@1:4) |

- l Both of these queries must have at least two channels in the chanlist, or an error will be generated.
- l The readings are returned sequentially in channel groups (i.e. xxxxxxxxyyyyyyyy … .) Where x represents all measurements for channel 1, y represents all measurements for channel 2 etc. Each data point takes up 64 bits. The values returned are 64-bit floating point numbers.
- l The &lt;values/chan&gt; parameter specifies the number of readings. So, for example, if (@1:4) is the specified channel list and values/ chan is specified as 10, a total of 40 values will be returned.
- l The FETCh? query does not erase measurements from the reading memory. You can send the query multiple times to retrieve the same data.
- l Use FETCh:CURRent:LOG:POINts? or FETCh:VOLTage:LOG:POINts? to query how many measurement points are available.
- l The instrument clears all measurements from reading memory whenever INITis executed.
- l If INITiate:TEST:MATChed has been configured for a different channel group than the channel group specified in this command, non-active channels will return +9.91000000e37 (Not-A-Number).

## FETCh:CURRent:MEDian:SUBtraction:LOG:POINts? FETCh:CURRent:MEDian:FIT:LOG:POINts?

Returns the number of processing algorithm values available per channel of the active channels specified in the INITcommand.

| Param eter                                        | TypicalReturn                                                        |
|---------------------------------------------------|----------------------------------------------------------------------|
| (none)                                            | 4020                                                                 |
| Returnsthenumber of Returnsthenumber of medianfit | mediansubtractionreadingsavailable:FE TC:CURR:ME D:SUBT :LO G:PO IN? |
| readingsavailable:FE TC:CURR:ME D:FIT :LO G:PO    | IN?                                                                  |

- l If you attempt to return more readings than are available, an error will be generated. You must include any offset/ chan values in the total number of readings available.

## FETCh:PROBecheck?(@&lt;chanlist&gt;)

Returns the boolean results of the probe check test. Returns lowest-numbered channel first.

| Param eter                                                   | TypicalReturn                                                                                              |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| (none)                                                       | Comma-separatedbooleanvaluesfromspecifiedchannels 0indicatesacell isNO Tpresent: 1indicatesacell ispresent |
| <chanlist>activechannelsfrom1- 32                            | (none)                                                                                                     |
| Returnstheprobecheckresultsfor channels1-4:FETC:PR OB?(@1:4) |                                                                                                            |

- l If INITiate:TEST has been configured for a different channel group than the channel group specified in this command, non-active channels will return 0.

## FETCh:TEMPerature:LATest?

Returns the most recent temperature of the external thermistor connected to the rear panel TEMP input (see Rear View).

| Param eter                                             | TypicalReturn                              |
|--------------------------------------------------------|--------------------------------------------|
| (none)                                                 | Comma-separatedvaluesfromspecifiedchannels |
| Returnsthelatest external temperature:FE TC:T EMP:LAT? |                                            |

- l SameasSYSTem:TEMPerature?EXTernal
- l The FETCh? query does not erase measurements from the reading memory. You can send the query multiple times to retrieve the same data.
- l The instrument clears all measurements from reading memory whenever INITis executed.

## FETCh:TEMPerature:LOG?&lt; values &gt; [,&lt; offset &gt;]

Returns the temperature measurement log of the external thermistor in ASCII.

| Param eter                                                                                           | TypicalReturn                 |
|------------------------------------------------------------------------------------------------------|-------------------------------|
| <values>thenumber of readingtoreturn                                                                 | Multiplecomma-separatedvalues |
| <offset>optional valuethat offsetsor skipsthenumber of readingsreturnedfromthebeginningof thedatalog | (none)                        |
| Skips5, thenreturnsthenext 10temperaturereadings:F ETC:T EMP:LO G?10,5                               |                               |

- l The FETCh? query does not erase measurements from the reading memory. You can send the query multiple times to retrieve the same data. 8192 is the maximum number of ASCII values that can be returned in any one call.
- l Use FETCh:TEMP:LOG:POINts? to query how many measurement points are available.
- l The instrument clears all measurements from reading memory whenever INITis executed.

## FETCh:TEMPerature:LOG:BINary? &lt; values &gt;

Returns the temperature measurement log of the external thermistor in binary. This command allows you to return all the data instead of being limited to 8192 values like ASCII readings. Use the FORMat:BORDer command to format the binary data.

| Param eter                                                   | TypicalReturn      |
|--------------------------------------------------------------|--------------------|
| <values>number of readingtoreturn                            | <binarydatastring> |
| Returns10temperaturereadingsinbinary:F ETC:T EMP:LO G:BIN?10 |                    |

- l Each data point (value) takes up 64 bits. The values returned are 64-bit floating point numbers.
- l The FETCh? query does not erase measurements from the reading memory.
- l Use FETCh:TEMP:LOG:POINts? to query how many measurement points are available.
- l The instrument clears all measurements from reading memory whenever INITis executed.

## FETCh:TEMPerature:LOG:POINts?

Returns the number of readings available in the temperature measurement log of the external thermistor.

| Param eter                                                           | TypicalReturn   |
|----------------------------------------------------------------------|-----------------|
| (none)                                                               | 4020            |
| Returnsthenumber of temperaturereadingsavailable:FE TC:T EMP:LO G:PO | IN?             |

- l If you attempt to return more readings than are available, an error will be generated. You must include any offset values in the total number of readings available.

## FETCh:VOLTage:OCV?(@&lt;chanlist&gt;)

Retrieves the open-circuit voltage (OCV) values. This command is only applicable when used in conjunction with the INITiate:TEST:OCV command.

| Param eter                                                                                 | TypicalReturn                                  |
|--------------------------------------------------------------------------------------------|------------------------------------------------|
| (none)                                                                                     | Comma-separatedO CVvaluesfromspecifiedchannels |
| <chanlist>activechannelsfrom1- 32                                                          | (none)                                         |
| ReturnstheO CVvaluesat thestart of thetest for thespecifiedchannels:FE TC:VOLT:O CV?(@1:4) |                                                |

- l If INITiate:TEST:MATChed has been configured for a different channel group than the channel group specified in this command, non-active channels will return +9.91000000e37 (Not-A-Number).

## Format Command

FORMat:BORDer NORMal|SWAPped

FORMat:BORDer?

Used for binary block transfers only. Selects the byte order for binary block transfers using FETCh?

| Param eter                               | TypicalReturn   |
|------------------------------------------|-----------------|
| NORMal&#124;SWAPped, *RSTSWAP            | SWAP            |
| Select thenormal byteorder:FORM:BORDNORM |                 |

- l In the NORMal byte order, the most-significant byte (MSB) of each data point is returned first and the least significant byte is returned last.
- l In the SWAPped byte order the least-significant byte (LSB) of each data point is returned first and the most significant byte is returned last.
- l The byte order setting is stored in non-volatile memory and does not change when power has been turned off.
- l The most common setting for this command is SWAPped.

## Initiate Commands

These commandsinitialize and start the discharge test.

![Image](%20BT2152B-prg_artifacts/image_000068_662ef697f96df1ac59ce0048aad305aaba94739a67e983126bad55a933433464.png)

You can only execute one INITiate:TESTat a time. For example, you cannot run INITiate:TEST:OCV on channel 1 while running INIT:TEST:MATCed on channel 2.

INITiate:TEST:MATChed&lt; time &gt;, &lt; ovp &gt;, &lt; uvp &gt;, &lt; res &gt;[,&lt; tint &gt;[,&lt; curr &gt;[,&lt; ocp &gt;]]], (@&lt;chanlist&gt;)

INITiate:TEST:MATChed? (@&lt;chanlist&gt;)

Sets all parameters for the voltage matched discharge current measurement. The query form returns the present INIT:TEST:MATCparameters for each channel in the list.

| Param eter                                                                                            | TypicalReturn   |
|-------------------------------------------------------------------------------------------------------|-----------------|
| <time>test durationinminutes(seetimeinterval <tint>betweensamples)                                    | 5               |
| <ovp>over-voltageprotectioninvolts:from0.5Vto4.5V;resolution:0.1mV                                    | 4.0             |
| <uvp>under-voltageprotectioninvolts:from0.5Vto4.5V;resolution:0.1mV                                   | 3.0             |
| <res>output resistanceinohms:from0.1 Ω to10 Ω (BT 2152A);0.05 Ω to10 Ω (BT 2152B);resolution: 0.001 Ω | 1.0             |
| optional <tint>timeinterval betweensamplesinseconds:from1to256                                        | 1               |
| optional <curr>initia l cell current inamperes:from-10mAto+10mA;resolution:0.1 μ A                    | 0.001           |
| optional <ocp>over-current protectioninamperes:from-10mAto+10mA;resolution:0.1 μ A                    | 0.01            |
| <chanlist>activechannels:from1- 32                                                                    | (none)          |

Configureschannels1:16for a6hour test withO V Pset to4.2V , UV Pset to1.8V , output resistance9 Ω , tim einterva l 10s, initia l ce ll current 0.5mA , over-current protect 1mA : INIT :T E S T :MA T C360, 4.2, 1.8, 9, 2, 0.0005, 0.001, (@1:16)

l Performing an in situ wiring resistance calibration immediately before the self-discharge measurement is recommended in order to obtain the best measurement results.

## Time Interval Parameter

The time interval &lt;tint&gt; parameter lets you specify an average time or time-between-samples where the data is averaged to return a single value. The range in the following tables is from 1 second to 250 seconds. The default time interval is 1 second. The recommended setting is 30 seconds, as this strikes a balance between seeing higher frequency events in the data and keeping the data record size manageable. As self-discharge is a slow process, a faster reading rate than 30 seconds is not typically required.

The following table describes maximum test times for some typical time intervals. To calculate the maximum test time in hours use Hours = (&lt;tint&gt; * 24)

## 4 Programming Reference

| Tim einterv al   | Maxim umtesttime   | Tim einterv al   | Maxim umtesttime   |
|------------------|--------------------|------------------|--------------------|
| 1second(default) | 1day               | 60seconds        | 60days             |
| 10seconds        | 10days             | 250seconds       | 250days            |

The following table gives the rate at which data can be returned based on the specified time interval

| Tim einterv al in seconds   |   Dataupdateratein seconds | Tim einterv al in seconds   |   Dataupdateratein seconds |
|-----------------------------|----------------------------|-----------------------------|----------------------------|
| 1- 4                        |                          4 | 33-64                       |                         64 |
| 5-8                         |                          8 | 65-128                      |                        128 |
| 9- 16                       |                         16 | 129-250                     |                        256 |
| 17-32                       |                         32 |                             |                            |

INITiate:TEST:OCV &lt; ovp &gt;, &lt; uvp &gt;, &lt; ocp &gt;, &lt; tint &gt;, (@&lt;chanlist&gt;)

INITiate:TEST:OCV? (@&lt;chanlist&gt;)

Initiates an open-circuit voltage test. The results can be retrieved with FETCh:VOLTage:OCV?. The query form returns the present INIT:TEST:OCV parameters for each channel in the list.

| Param eter                                                                | TypicalReturn   |
|---------------------------------------------------------------------------|-----------------|
| <ovp>over-voltageprotectioninvolts:from0.5Vto4.5V;resolution:0.1mV        | 4.0             |
| <uvp>under-voltageprotectioninvolts:from0.5Vto4.5V;resolution:0.1mV       | 3.0             |
| <ocp>over-current protectioninamperes:from-10mAto+10mA;resolution:0.1 μ A | 0.01            |
| <tint>theaveragingtimeinseconds:from1to256                                | 1               |
| <chanlist>activechannels:from1- 32                                        | (none)          |

Configureschannels1:16for a6hour test withO V Pset to4.2V , UV Pset to1.8V , output resistance9 Ω , tim einterva l 10s, initia l cell current 0.5mA , over-current protect 1m A : IN IT :T E S T :O C V4.2, 1.8, 0.001, 2, (@ 1:16)

## INITiate:TEST:PROBecheck (@&lt;chanlist&gt;)

Initiates a probe check test to determine if a cell is connected to the specified channels in the channel list. Send FETCh:PROBecheck? to return the results of the probe check. Send SENSe:PROBecheck:AVAIlable?to check whether a probe check test has completed.

| Param eter                                                   | TypicalReturn   |
|--------------------------------------------------------------|-----------------|
| (none)                                                       | (none)          |
| Initiateaprobechecktest on16channels:INIT :T EST:PROB(@1:16) |                 |

## LXI Command

## LXI:IDENtify[:STATe] 0|OFF|1|ON LXI:IDENtify[:STATe]?

Turns the front panel LAN light on or off. When turned on, the LAN status light on the front panel blinks on and off to identify the instrument that is being addressed.

| Param eter                                 | TypicalReturn   |
|--------------------------------------------|-----------------|
| 0&#124;O FF&#124;1&#124;ON                 | 0 or 1          |
| Toblinkthefront panel LANlight:LX I:IDENON |                 |

## Output Commands

## OUTPut:INHibit:MODELATChing|LIVE|OFF OUTPut:INHibit:MODE?

Sets the operating mode of the Inhibit Input digital pin (pin 3). The inhibit function disconnects all input channels from the cells in response to an external signal on the Inhibit input pin. See Understanding the Digital Port.

LATChing - a logic-true signal on the Inhibit input causes the input channels to disconnect. The channels remain disconnected until the Inhibit input is returned to logic-false and the latched INH status bit is cleared by sending the OUTPut:PROTection:CLEar command.

LIVE - allows the input channels to follow the state of the Inhibit input. When the Inhibit input is true, the channels are disconnected. When the Inhibit input is false, the channels are re-connected.

OFF - The Inhibit input is ignored.

| Param eter                                          | TypicalReturn    |
|-----------------------------------------------------|------------------|
| LAT Ching&#124;LIVE&#124;O FF,*RSTO FF              | LAT C,LIVE,orOFF |
| SetstheInhibit Input toLivemode:O UTP:INH:MO DELIVE |                  |

- l The front panel Error light turns on when any inhibit signal (live or latched) occurs. To clear the Error light, remove the inhibit signal and send the OUTPut:PROTection:CLEar command.

## OUTPut:PROTection:CLEar

Resets any protection events, inhibits, or errors that have occurred. The protection settings are specified in the INIT:TEST commands.

| Param eter                                 | TypicalReturn   |
|--------------------------------------------|-----------------|
| (none)                                     | (none)          |
| Clear instrument protection:OUTP:PR OT:CLE |                 |

## Sense Commands

## SENSe:OCV:AVAIlable?

Returns the availability of the open-circuit voltage measurement. This command is only applicable when used in conjunction with the INITiate:TEST:OCV command.

Aone(1) is returned when the OCV measurement is completed. A zero (0) is returned when the OCV measurement is unavailable or if the command was used with any other INITcommand besides INITiate:TEST:OCV.

| Param eter                                   | TypicalReturn   |
|----------------------------------------------|-----------------|
| (none)                                       | 0or1            |
| ReturnstheavailabilityofOCV:SE NS:O CV:AVAI? |                 |

## SENSe:PROBecheck:AVAIlable?

Returns the availability of the probe check test.

Aone(1) is returned when the probe check command is completed. A zero (0) is returned when the probe check command is unavailable.

| Param eter                                                  | TypicalReturn   |
|-------------------------------------------------------------|-----------------|
| (none)                                                      | 0or1            |
| Returnstheavailabilityof theProbechecktest:SENS:PR OB:AVAI? |                 |

SENSe:THERmistor:CONFigure &lt; temp &gt;, &lt; resistance &gt;, &lt; beta &gt;

SENSe:THERmistor:CONFigure?

Specifies the parameters for the external thermistor connected to the rear panel temperature sensor input (see Thermistor Connections).

| Param eter                                                                       | TypicalReturn   |
|----------------------------------------------------------------------------------|-----------------|
| <temp>thenominal temperatureof thethermistor indegreesC ,from-272.15°Cto273.15°C | 25°C            |
| <resistance>thenominal resistanceinohms,from1 Ω to1,000,000 Ω                    | 10,000          |
| <beta>valuefrom1to1,000,000                                                      | 4073            |
| Specifiesthenominal temperatureandresistance:SENS:T HER:C ONF25,10000,4073       |                 |

## SENSe:TTIMe:REMaining?

Returns the remaining test time in minutes for the test that is presently running.

## 4 Programming Reference

| Param eter                                   | TypicalReturn   |
|----------------------------------------------|-----------------|
| (none)                                       | 2.200000E +02   |
| Returnstheremainingtest time:SENS:T TIM:REM? |                 |

## SENSe:VERification:AVAIlable?

Returns the state of the verification procedure. A one (1) is returned when the verification procedure is completed. A zero (0) is returned when the verification is in progress (see CALibration:VERification:STARt). .

| Param eter                                                  | TypicalReturn   |
|-------------------------------------------------------------|-----------------|
| (none)                                                      | 0or1            |
| Returnsthestateof theverificationprocedure:SENS:VE R:A VAI? |                 |

## SENSe:WIRE:RESistance:AVAIlable?

Returns the state of the wire resistance calibration. A one (1) is returned when the wire resistance calibration is completed and the wire resistance values are available. A zero (0) is returned when the calibration is in progress.

| Param eter                                                            | TypicalReturn   |
|-----------------------------------------------------------------------|-----------------|
| (none)                                                                | 0or1            |
| Returnsthestateof thewireresistancecalibration:SENS:WIR E:R ES:A VAI? | 0or1            |

&gt;, (@&lt;chanlist&gt;)

## SENSe:WIRE:RESistance:CONFigure &lt; resistance SENSe:WIRE:RESistance:CONFigure?(@&lt;chanlist&gt;)

This command is synonymous with CALibration:WIRE:RESistance:VALues. It sets the wiring resistance of the specified channels. The query returns the presently set wiring resistance of the specified channels. Refer to Wire Resistance Calibration for more information.

| Param eter                                                                       | TypicalReturn   |
|----------------------------------------------------------------------------------|-----------------|
| <resistance>wireresistanceinohms,from0 Ω to5 Ω ; resolution:0.001 Ω ; Default:0  | 0               |
| <chanlist>activechannelsfrom1- 32                                                | (none)          |
| Specifiesawireresistanceof 0.188 Ω for channel 1:SENS:WIR E:R ES:C ONF0.188,(@1) |                 |

## NOTE

Wire resistance calibration is required when all cell connectors have been installed in the instrument. Wire resistance calibration is also required whenever any cell connector is unplugged, reinserted, or reseated.

## StatusCommands

Status commandslet you determine the operating condition of the instrument at any time. Refer to Status Tutorial for more information.

## STATus:ALARm[EVENt]?

Returns the sum of the bits in the event register for the Status Alarm Register group. An event register is a read-only register that latches events from the condition register. While an event bit is set, subsequent events corresponding to that bit are ignored. The register bits are cleared when you read the register.

| Param eter                             | TypicalReturn   |
|----------------------------------------|-----------------|
| (none)                                 | <bit value>     |
| Readtheevent alarmregister:STAT :ALAR? |                 |

- l Once a bit is set, it remains set until cleared by reading the event register or by sending *CLS (clear status).
- l The value returned is the binary-weighted sum of all bits set in the register.

## STATus:ALARm:CONDiton?

Returns the sum of the bits in the condition register for the Status Alarm Register group. Condition register bits are updated in real time; they are neither latched nor buffered. This register is read-only; bits are not cleared when read. The alarm status group consists of the OVP, UVP, and OCP status bits in the Status Questionable registers.

| Param eter                                  | TypicalReturn   |
|---------------------------------------------|-----------------|
| (none)                                      | <bit value>     |
| Readtheevent alarmregister:STAT :ALAR:COND? |                 |

- l The condition register bits reflect the current condition. If a condition goes away, the corresponding bit is cleared in the condition register.
- l The value returned is the binary-weighted sum of all bits set in the register.

## STATus:ALARm:ENABle &lt; value &gt; STATus:ALARm:ENABle?

Enables bits in the condition register for the Status Alarm Register group. The selected bits are then reported to the Status Byte. An enable register defines which bits in the event register will be reported to the Status Byte register group. You can write to or read from an enable register.

## 4 Programming Reference

| Param eter                                                                     | TypicalReturn        |
|--------------------------------------------------------------------------------|----------------------|
| Adecimal valuethat correspondstothebinary- weightedsumof thebitsintheregister. | +259(bit 1,2and8set) |
| Enablebits1,2,and8intheenableregister:STAT :A LAR:E NAB259                     |                      |

- l Use the &lt;value&gt; parameter to specify which bits will be reported to the Status Byte. The decimal value specified corresponds to the binary-weighted sum of the bits you wish to enable in the register.
- l The enable setting value is stored in nonvolatile memory.

## STATus:ALARm:CONDiton:CURRent?

Returns the sum of the bits feeding the over-current (OCP) condition bit in the Status Alarm Register group. This is a 32-bit unsigned value, where each bit represents one channel. Channel 1 is represented by bit 0; channel 32 by bit 31.

| Param eter                                        | TypicalReturn   |
|---------------------------------------------------|-----------------|
| (none)                                            | <bit value>     |
| Readtheevent alarmregister:STAT :ALAR:C OND:CURR? |                 |

- l The condition register bits reflect the current condition. If a condition goes away, the corresponding bit is cleared in the condition register.
- l The value returned is the binary-weighted sum of all bits set in the register.

## STATus:ALARm:CONDiton:VOLTage?

Returns the sum of the bits feeding the over-voltage (OVP) condition bit in the Status Alarm Register group. This is a 32-bit unsigned value, where each bit represents one channel. Channel 1 is represented by bit 0; channel 32 by bit 31.

| Param eter                                        | TypicalReturn   |
|---------------------------------------------------|-----------------|
| (none)                                            | <bit value>     |
| Readtheevent alarmregister:STAT :ALAR:COND:VO LT? |                 |

- l The condition register bits reflect the current condition. If a condition goes away, the corresponding bit is cleared in the condition register.
- l The value returned is the binary-weighted sum of all bits set in the register.

## STATus:ALARm:CONDiton:VOLTage:UNDer?

Returns the sum of the bits feeding the under-voltage (UVP) condition bit in the Status Alarm Register group. This is a 32-bit unsigned value, where each bit represents one channel. Channel 1 is represented by bit 0; channel 32 by bit 31.

| Param eter                                             | TypicalReturn   |
|--------------------------------------------------------|-----------------|
| (none)                                                 | <bit value>     |
| Readtheevent alarmregister:STAT :ALAR:COND:VO LT :UND? |                 |

- l The condition register bits reflect the current condition. If a condition goes away, the corresponding bit is cleared in the condition register.
- l The value returned is the binary-weighted sum of all bits set in the register.

## STATus:ALARm:ENABle &lt; value &gt; STATus:ALARm:ENABle?

Enables bits in the condition register for the Status Alarm Register group. The selected bits are then reported to the Status Byte. An enable register defines which bits in the event register will be reported to the Status Byte register group. You can write to or read from an enable register.

| Param eter                                                                     | TypicalReturn   |
|--------------------------------------------------------------------------------|-----------------|
| Adecimal valuethat correspondstothebinary- weightedsumof thebitsintheregister. | +16(bit 4set)   |
| Enablebit 4(value16)intheenableregister:STAT :A LAR:E NAB16                    |                 |

- l Use the &lt;value&gt; parameter to specify which bits will be reported to the Status Byte. The decimal value specified corresponds to the binary-weighted sum of the bits you wish to enable in the register. For example, to enable bit 4 (decimal value = 16) and bit 8 (decimal value = 256), the corresponding decimal value would be 272 (16 + 256).
- l The enable setting value is stored in nonvolatile memory.

## STATus:OPERation[:EVENt]?

Returns the sum of the bits in the event register for the Standard Operation Register group. An event register is a read-only register that latches events from the condition register. While an event bit is set, subsequent events corresponding to that bit are ignored. The register bits are cleared when you read the register.

| Param eter                                        | TypicalReturn   |
|---------------------------------------------------|-----------------|
| (none)                                            | <bit value>     |
| Readtheoperationevent statusregister:STAT :O PER? |                 |

- l Once a bit is set, it remains set until cleared by reading the event register or by sending *CLS (clear status).
- l The value returned is the binary-weighted sum of all bits set in the register.

## STATus:OPERation:CONDition?

Returns the sum of the bits in the condition register for the Standard Operation Register group. This register is read-only; bits are not cleared when read.

Acondition register continuously monitors the state of the instrument. Condition register bits are updated in real time; they are neither latched nor buffered

| Param eter                                                | TypicalReturn   |
|-----------------------------------------------------------|-----------------|
| (none)                                                    | <bit value>     |
| Readtheoperationstatusconditionregister:STAT :O PER:COND? |                 |

- l The condition register bits reflect the current condition. If a condition goes away, the corresponding bit is cleared.
- l The value returned is the binary-weighted sum of all bits set in the register.

## STATus:OPERation:ENABle &lt; value &gt; STATus:OPERation:ENABle?

Sets and queries bits in the enable register for the Standard Operation Register group. The enable register is a mask for enabling specific bits from the Operation Event register to set the OPER (operation summary) bit of the Status Byte register. STATus:PRESet clears all bits in the enable register.

| Param eter                                                                     | TypicalReturn   |
|--------------------------------------------------------------------------------|-----------------|
| Adecimal valuethat correspondstothebinary- weightedsumof thebitsintheregister. | +16(bit 4set)   |
| Enablebit 4intheenableregister:STAT :O PER:E NAB16                             |                 |

- l *CLSdoes not clear the enable register, but does clear the event register.

## System Commands

## SYSTem:COMMunicate:ENABle 0|OFF|1|ON, &lt; interface &gt;

SYSTem:COMMunicate:ENABle?&lt; interface &gt;

Disables or enables the USB or LAN interface. You must cycle power for the changes to take effect.

| Param eter                                              | TypicalReturn   |
|---------------------------------------------------------|-----------------|
| 0&#124;O FF&#124;1&#124;O NDefault:ONfor all interfaces | 0 or 1          |
| <interface>USB&#124;LAN                                 | (none)          |
| DisabletheUSBinterface:SY ST:COMM:E NABOFF,USB          |                 |

- l If you disable the LAN interface, none of the associated LAN services will start at power-on.
- l The interface enable settings are stored in nonvolatile memory.

## SYSTem:COMMunicate:LAN:CONTrol?

Returns the initial socket control connection port number. This connection is used to send and receive commandsand queries.

| Param eter                                                   | TypicalReturn              |
|--------------------------------------------------------------|----------------------------|
| (none)                                                       | <port #>                   |
|                                                              | (0if socketsnot supported) |
| QuerytheC ontrol connectionport number:SY ST:C OMM:LAN:CONT? |                            |

- l Use the Control socket connection to send a Device Clear (DCL) to the instrument or to detect pending Service Request (SRQ) events.

## SYSTem:COMMunicate:LAN:DHCP0|OFF|1|ON SYSTem:COMMunicate:LAN:DHCP?

Disables or enables instrument'suse of DHCP. DHCPstands for Dynamic Host Configuration Protocol, a protocol for assigning dynamic IP addresses to networked devices. With dynamic addressing, a device can have a different IP address every time it connects to the network.

ON - the instrument tries to obtain an IP address from a DHCP server. If a DHCP server is found, it assigns a dynamic IPaddress, Subnet Mask, and Default Gateway to the instrument.

OFForDHCPunavailable - the instrument uses the static IP address, Subnet Mask, and Default Gateway during power-on.

| Param eter                             | TypicalReturn   |
|----------------------------------------|-----------------|
| 0&#124;O FF&#124;1&#124;O N,Default:ON | 0 or 1          |
| DisableDHC P:SY ST:COMM:LAN:DHCPO FF   |                 |

## 4 Programming Reference

- l If a DHCPLAN address is not assigned by a DHCP server, then an Auto-IP address is obtained after approximately 2 minutes. An Auto-IP address has the form 169.254.nnn.nnn.
- l The DHCPsetting is stored in non-volatile memory.

![Image](%20BT2152B-prg_artifacts/image_000069_f9059a5a6cf156bb55617166aaff62e159e6adedb616868722577c9f9f1421f1.png)

If you change this setting, you must send SYSTem:COMMunicate:LAN:UPDate to activate the new setting.

## SYSTem:COMMunicate:LAN:DNS[1|2] "&lt; address &gt;" SYSTem:COMMunicate:LAN:DNS[1|2]?[CURRent|STATic]

Assigns the static IP addresses of Domain Name System (DNS) servers. A primary and a secondary server address may be assigned. If DHCPis available and enabled, DHCPwill auto-assign these server addresses. These auto-assigned server addresses take precedence over the static addresses assigned with this command. Contact your LAN administrator for details.

The optional query CURRent parameter returns the address currently being used by the instrument. The optional query STATic parameter returns the static address from non-volatile memory. This address is used if DHCPis disabled or unavailable.

| Param eter                                                        | TypicalReturn                                                     |
|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Command:"nnn.nnn.nnn.nnn".Default:"0.0.0.0".                      | (none)                                                            |
| Query:[C URRent&#124;ST ATic].Default:CURRent                     | "198.105.232.4"                                                   |
| Toset astaticprimaryDNSaddress:SY ST:C OMM:LAN:DNS"198.105.232.4" | Toset astaticprimaryDNSaddress:SY ST:C OMM:LAN:DNS"198.105.232.4" |

- l The assigned DNS server addresses are used if DHCP is disabled or unavailable. Otherwise, the DNS server addresses are auto-assigned by DHCP.
- l The DNSserver addresses are stored in non-volatile memory.

![Image](%20BT2152B-prg_artifacts/image_000070_f9059a5a6cf156bb55617166aaff62e159e6adedb616868722577c9f9f1421f1.png)

If you change this setting, you must send SYSTem:COMMunicate:LAN:UPDate to activate the new setting.

## SYSTem:COMMunicate:LAN:DOMain?

Returns the domain name assigned to the instrument.

| Param eter   | TypicalReturn   |
|--------------|-----------------|
| (none)       | "example.com"   |

Returnthedomainnameusedbytheinstrument:SY S T :C O MM:LA N:DO M?

- l If Dynamic Domain Name System (DNS) is available on your network and your instrument uses DHCP, the domain name is assigned by the Dynamic DNS service at power-on.
- l Anull string ("") indicates that no domain name is assigned.

## SYSTem:COMMunicate:LAN:GATeway "&lt; address &gt;" SYSTem:COMMunicate:LAN:GATeway?[CURRent|STATic]

Assigns a default gateway for the instrument. The specified IP Address sets the default gateway, which allows the instrument to communicate with systems that are not on the local subnet. Thus, this is the default gateway where packets are sent that are destined for a device not on the local subnet, as determined by the Subnet Mask setting. Contact your LAN administrator for details.

The optional query CURRent parameter returns the address currently being used by the instrument. The optional query STATic parameter returns the static address from non-volatile memory. This address is used if DHCPis disabled or unavailable.

| Param eter                                                         | TypicalReturn   |
|--------------------------------------------------------------------|-----------------|
| Command:"nnn.nnn.nnn.nnn".Default:"0.0.0.0".                       | (none)          |
| Query:[C URRent&#124;ST ATic].Default:CURRent                      | "198.105.232.1" |
| Toset astaticprimaryDNSaddress:SY ST:C OMM:LAN:G AT"198.105.232.1" |                 |

- l If DHCPis enabled, the specified default gateway is not used. However, if the DHCP server fails to assign a valid IP address, the currently configured default gateway is used.
- l The gateway address is stored in non-volatile memory.

![Image](%20BT2152B-prg_artifacts/image_000071_dad78c936d19a0a917c1a631a065cf5372b4df33a50615b0917ea37015336a78.png)

If you change this setting, you must send SYSTem:COMMunicate:LAN:UPDate to activate the new setting.

## SYSTem:COMMunicate:LAN:HOSTname "&lt; name &gt;" SYSTem:COMMunicate:LAN:HOSTname?[CURRent|STATic]

Assigns a hostname to the instrument. A hostname is the host portion of the domain name, which is translated into an IP address. If Dynamic Domain Name System (Dynamic DNS) is available on your network and your instrument uses DHCP, the hostname is registered with the Dynamic DNS service at power-on. If DHCPis enabled, the DHCPserver can change the specified hostname. Contact your LAN administrator for details.

The optional query CURRent parameter returns the name currently being used by the instrument. The optional query STATic parameter returns the name from non-volatile memory. This may not be the actual name used by the instrument if DHCPis enabled.

| Param eter                                                                                              | TypicalReturn      |
|---------------------------------------------------------------------------------------------------------|--------------------|
| Stringof upto15characters.Must start withletter (A -Z)Maycontain letters, numbers(0-9), or dashes("-"). | (none)             |
| Query:[C URRent&#124;ST ATic].Default:CURRent                                                           | "Keysight BT2152B" |
| Todefineahostname:SY ST:COMM:LAN:HO ST"Keysight BT2152B                                                 |                    |

## 4 Programming Reference

- l If no hostname exists, the query returns a null string ("").
- l The hostname is stored in non-volatile memory.

![Image](%20BT2152B-prg_artifacts/image_000072_116f6c49fc402a69d36dfe312ca4bf151efdae22c7f3aaccca08cdccb210dc88.png)

If you change this setting, you must send SYSTem:COMMunicate:LAN:UPDate to activate the new setting.

## SYSTem:COMMunicate:LAN:IPADdress"&lt; address &gt;" SYSTem:COMMunicate:LAN:IPADdress?[CURRent|STATic]

Assigns a static Internet Protocol (IP) address for the instrument. If DHCP is enabled, the specified static IP address is not used. Contact your LAN administrator for details.

The optional query CURRent parameter returns the address currently being used by the instrument. The optional query STATic parameter returns the static address from non-volatile memory. This address may not be the actual address used by the instrument if DHCPis enabled.

| Param eter                                                  | TypicalReturn    |
|-------------------------------------------------------------|------------------|
| Command:"nnn.nnn.nnn.nnn".                                  | (none)           |
| Query:[C URRent&#124;ST ATic].Default:CURRent               | "169.254.149.35" |
| Toset astaticIPaddress:SY ST:C OMM:LAN:IPAD"169.254.149.35" |                  |

- l The IP address is stored in non-volatile memory.

![Image](%20BT2152B-prg_artifacts/image_000073_662ef697f96df1ac59ce0048aad305aaba94739a67e983126bad55a933433464.png)

If you change this setting, you must send SYSTem:COMMunicate:LAN:UPDate to activate the new setting.

## SYSTem:COMMunicate:LAN:MAC?

Returns the instrument'sMedia Access Control (MAC) address as an ASCII string of 12 hexadecimal characters (0-9 and A-F) enclosed in quotation marks.

| Param eter                                 | TypicalReturn   |
|--------------------------------------------|-----------------|
| (none)                                     | "0030D3001041"  |
| ToreturntheMACaddress:SY ST:C OMM:LAN:MAC? |                 |

- l The MACaddress is also known as the link-layer address, the Ethernet (station) address, LANIC ID or Hardware Address. This is an unchangeable 48-bit address assigned by the manufacturer to each unique Internet device.

| Your LAN administrator mayneed theMACaddressto assign a static IPaddress for this   |
|-------------------------------------------------------------------------------------|
| device.                                                                             |

## SYSTem:COMMunicate:LAN:SMASk "&lt; mask &gt;" SYSTem:COMMunicate:LAN:SMASk?[CURRent|STATic]

Assigns a subnet mask for the instrument to use in determining whether a client IP address is on the samelocal subnet. When a client IPaddress is on a different subnet, all packets must be sent to the Default Gateway. Contact your LAN administrator for details.

The optional query CURRent parameter returns the address currently being used by the instrument. The optional query STATic parameter returns the static address from non-volatile memory. This address is used if DHCPis disabled or unavailable..

| Param eter                                           | TypicalReturn   |
|------------------------------------------------------|-----------------|
| Command:"nnn.nnn.nnn.nnn".Default:"255.255.0.0".     | (none)          |
| Query:[C URRent&#124;ST ATic].Default:CURRent        | "255.255.0.0"   |
| Toset asubnet mask:SY ST:C OMM:LAN:IPAD"255.255.0.0" |                 |

- l If DHCPis enabled (SYSTem:COMMunicate:LAN:DHCPON), the specified subnet mask is not used. However, if the DHCPserver fails to assign a valid IP address, the instrument uses the Auto-IP subnet mask.
- l Avalue of "0.0.0.0" or "255.255.255.255" indicates that subnetting is not being used.
- l The subnet mask setting is stored in non-volatile memory.

NOTE

If you change this setting, you must send SYSTem:COMMunicate:LAN:UPDate to activate the new setting.

## SYSTem:COMMunicate:LAN:TELNet:PROMpt "&lt; string &gt;" SYSTem:COMMunicate:LAN:TELNet:PROMpt?

Specifies the command prompt seen when communicating with the instrument via Telnet.

| Param eter                                                | TypicalReturn   |
|-----------------------------------------------------------|-----------------|
| Quotedstringof upto15characters.Default: "BT 2152B".      | "BT 2152B"      |
| Toset acommandprompt:SY ST:C OMM:LAN:T ELN:PR OM"BT2152B" |                 |

- l The instrument uses LAN port 5024 for SCPI Telnet sessions and port 5025 for SCPI Socket sessions.
- l Telnet sessions are typically started from a host computer shell (telnet &lt;IP\_address&gt; &lt;port&gt;). For example: telnet 169.254.4.10 5024

To exit a Telnet session, press &lt;Ctrl-D&gt;.

- l This setting is stored in non-volatile memory.

## SYSTem:COMMunicate:LAN:TELNet:WMESsage "&lt; string &gt;" SYSTem:COMMunicate:LAN:TELNet:WMESsage?

Specifies the welcome message seen when communicating with the instrument via Telnet.

| Param eter                                                                    | TypicalReturn                 |
|-------------------------------------------------------------------------------|-------------------------------|
| Quotedstringof upto63characters.Default:"Welcome totheT elnet Session".       | "WelcometotheT elnet Session" |
| Toset acommandprompt: SY ST:C OMM:LAN:TELN:WME S"WelcometotheT elnet Session" |                               |

- l The instrument uses LAN port 5024 for SCPI Telnet sessions and port 5025 for SCPI Socket sessions.
- l This setting is stored in non-volatile memory.

## SYSTem:COMMunicate:LAN:UPDate

Stores any changes made to the LAN settings into non-volatile memory and restarts the LAN driver with the updated settings.

| Param eter   | TypicalReturn   |
|--------------|-----------------|
| (none)       | (none)          |

Thefollowingconfigurestheinstrument tousestaticallyassignedLA Nsettings:

SY S T :C O M M :L A N :D H C PO F F

SY S T :C O M M :L A N :D N S"198.105.232.4"

SY S T :C O M M :L A N :D N S 2 "198.105.232.5"

SY S T :C O M M :L A N :G A T"198.105.232.1"

SY S T :C O M M :L A N :H O S T"L A B 1-D M M "

SY S T :C O M M :L A N :IP A D"198.105.232.101"

SY S T :C O M M :L A N :S M A S"255.255.255.0"

SY S T :C O M M :L A N :W IN S"198.105.232.4"

SY S T :C O M M :L A N :W IN S"198.105.232.5"

SY S T :C O M M :L A N :U P D

Thefollowingconfigurestheinstrument backtouseDHC P :

SY S T :C O M M :L A N :D H C PO N

SY S T :C O M M :L A N :U P D

- l This command must be sent after changing the settings for DHCP, DNS, gateway, hostname, IP address, subnet mask, or WINS.
- l Make all changes to the LAN settings before sending this command.

## SYSTem:COMMunicate:LAN:WINS[1|2] "&lt; address &gt;" SYSTem:COMMunicate:LAN:WINS[1|2]?[CURRent|STATic]

Assigns the static IP addresses of the Windows Internet Name System (WINS) servers. A primary and a secondary server address may be assigned. If DHCPis available and enabled, DHCPwill auto-assign these server addresses. These auto-assigned server addresses take precedence over the static addresses assigned with this command. Contact your LAN administrator for details.

The optional query CURRent parameter returns the address currently being used by the instrument. The optional query STATic parameter returns the static address from non-volatile memory. This address is used if DHCPis disabled or unavailable.

| Param eter                                                         | TypicalReturn   |
|--------------------------------------------------------------------|-----------------|
| Command:"nnn.nnn.nnn.nnn".Default:"0.0.0.0".                       | (none)          |
| Query:[C URRent&#124;ST ATic].Default:CURRent                      | "198.105.232.4" |
| Toset astaticprimaryWINSaddress:SY ST:C OMM:LAN:DNS"198.105.232.4" |                 |

- l The WINSaddresses are stored in non-volatile memory.

![Image](%20BT2152B-prg_artifacts/image_000074_0a1deec5f1eb8c3a4859b2460ecbc807d2ccb9133ab3af574f0149a7adfa45ef.png)

If you change this setting, you must send SYSTem:COMMunicate:LAN:UPDate to activate the new setting.

SYSTem:DATE&lt; yyyy &gt;, &lt; mm &gt;, &lt; dd &gt;

SYSTem:DATE?

SYSTem:TIME&lt;

hh &gt;, &lt; mm &gt;, &lt; ss &gt;

SYSTem:TIME?

SYSTem:DATE- Setsthe date of the system clock. Specify the year (2000 to 2099), month (1 to 12), and day (1 to 31).

SYSTem:TIME- Sets the time of the system clock. Specify hours (0 to 23), minutes (0 to 59), and seconds (0 to 59).

| Param eter                                                                              | TypicalReturn   |
|-----------------------------------------------------------------------------------------|-----------------|
| <yyyy>,<mm>,<dd>                                                                        | +2024,+03,+30   |
| <hh>,<mm>,<ss>                                                                          | 20,30,00.000    |
| Set thedatetoMarch30,2024:SY ST:DAT E2024,03,30 Set theclockto8:30PM:SY ST:T IME20,30,0 |                 |

## SYSTem:ERRor?

Readsand clears one error from the error queue.

| Param eter                                             | TypicalReturn   |
|--------------------------------------------------------|-----------------|
| (none)                                                 | +0,"Noerror"    |
| Readsandclearsthefirst error inerror queue:SY ST:E RR? |                 |

## 4 Programming Reference

- l Error retrieval is first-in-first-out (FIFO), and errors are cleared as you read them.
- l If more have accumulated than the queue can hold, the last error stored in the queue (the most recent error) is replaced with -350,"Error queue overflow". No additional errors are stored until you remove errors from the queue. If no errors have occurred when you read the error queue, the instrument responds with +0,"No error".
- l The error queue is cleared when power is cycled. It is not cleared by a *RST.
- l Errors have the following format (the error string may contain up to 80 characters). &lt; error code &gt;,&lt; error string &gt; For a list of error codes and message strings, see SCPI Error Messages.

## SYSTem:LICense:CATalog?

Returns the channel license of the unit. The value returned is the number of available channels. Values can range from 004 to 032 in increments of 4 channels. Channel numbering on the back of the unit is from left to right.

| Param eter                                             | TypicalReturn            |
|--------------------------------------------------------|--------------------------|
| (none)                                                 | 032(32availablechannels) |
| Returnsthenumber of availablechannels:SY ST:LIC :C AT? |                          |

## SYSTem:TEMPerature?EXTernal

Returns the temperature sensed across a 10 k Ω thermistor, which must be connected to the rear panel TEMPinput in °C(see Rear View).

| Param eter                                                   | TypicalReturn     |
|--------------------------------------------------------------|-------------------|
| EX Ternal                                                    | +2.41923802E +001 |
| Returnthetemperatureof theexternal thermistor:SY ST:TEMP?EXT |                   |

- l If nothing is connected to the external temperature connector, the command will return 9.91E37.

## StatusTutorial

StatusRegisters

Alarm Channel Groups

Alarm StatusGroup

Standard Operation Group

StatusByte Register

Error and Output Queues

## StatusDiagram

This section provides a detailed description of the individual registers and register groups. The status diagram at the end of this topic shows how the status registers and groups are interconnected.

## StatusRegisters

The Alarm Channel, Alarm Status, and Standard Operation groups use three different types of registers to track qualify, flag, and enable instrument events.

- l ACondition register continuously monitors the state of the instrument. The bits in the condition register are updated in real time and the bits are not latched or buffered.
- l An Event register latches the various events from the condition register. There is no buffering in this register; while an event bit is set, subsequent events corresponding to that bit are ignored. This is a read-only register.
- l An Enable register defines which bits in the event register will be reported to the Status Byte register group. You can write to or read from an enable register.

To program individual bits in any register group, you must send a value that corresponds to the binaryweighted value of all the bits that you wish to enable. For example, to enable bit 2 (decimal value = 4) and bit 4 (decimal value = 16), the corresponding decimal value would be 20 (4 + 16).Similarly, any register queries return the binary-weighted value of the bits that have been set. For example, with bit 3 (value 8) and bit 5 (value 32) being set, the query returns +40.

## Alarm Channel Groups

These registers record signals that indicate abnormal conditions on specific channels. There are three condition groups - one for each abnormal condition: over-voltage, over-current, and under-voltage.

The group channel assignments are 32-bit unsigned values where each bit represents one channel. Channel 1 is represented by bit 0; channel 32 by bit 32. A '1' in a bit position indicates that the indicated alarm condition is true. When true, the affected channel is shut down.

The channel bits are logically-ORed into bits 0, 1, and 9 of the Alarm Status Group. The following table describes the bit assignments.

## 4 Programming Reference

| Bit   | BitName     | Decim alValue   |
|-------|-------------|-----------------|
| 0     | Channel 1 1 |                 |
| 1     | Channel 2 2 |                 |
| 2     | Channel 3   | 4               |
| 3     | Channel 4   | 8               |
| .     | .           | .               |
| .     | .           | .               |
| .     | .           | .               |
| 29    | Channel 30  | 536870912       |
| 30    | Channel 31  | 1073741824      |
| 31    | Channel 32  | 2147483648      |

## Alarm StatusGroup

These register groups record signals that indicate abnormal operation. The group consists of a Condition, Event, and Enable register. The outputs of the Alarm Status group are logically-ORed into the QUEStionable summary bit (3) of the Status Byte register. Refer to Status Registers for a description of each register. The following table describes the bit assignments.

| Bit      |   BitName | Decim alValue           | Defin ition   |
|----------|-----------|-------------------------|---------------|
| OVP      |         1 | Over-voltageprotection  | 0             |
| OCP      |         2 | Over-current protection | 1             |
| not used |           | 0isreturned             | 2-8 not used  |
| UVP      |       512 | Under-voltageprotection | 9             |
| not used |           | not used 0isreturned    | 10-15         |

## Standard Operation Group

This register group records signals that indicate the present operating status of the instrument. The group consists of a Condition, Event, and Enable register. The Standard Operation event register latches events relating to the operation of the unit. It is a read-only register that is cleared when read. The Standard Operation enable register functions similarly to the enable registers of the Alarm Status group. Refer to Status Registers for a description of each register. The following table describes the bit assignments.

| Bit   | BitName                  | Decim alValue   | Defin ition                                                                                                          |
|-------|--------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------|
| 0     | Calibrating              | 1               | Calibrationisinprogress.                                                                                             |
| 1     | WarmUp                   | 2               | Theinstrument iswarmingup.                                                                                           |
| 2     | EmergencyStop            | 4               | Anemergencystopconditionhasbeenactivated.                                                                            |
| 3     | not used                 | not used        | 0isreturned                                                                                                          |
| 4     | Measuring                | 16              | Acell measurement isinprogress.                                                                                      |
| 5-7   | not used                 | not used        | 0isreturned                                                                                                          |
| 8     | Configchanged            | 256             | Thecell configurationhaschangedsincetheprevioustest hasrun.                                                          |
| 9     | Inhibit                  | 512             | Theinhibit input signal hasdisconnectedall channelsfromthecells.                                                     |
| 10-11 | not used                 | not used        |                                                                                                                      |
| 12    | Temperatureunreg- ulated | 4096            | Thereferencetemperatureof theinstrument cannot bemaintainedwithinspe- cificationsduringtheexecutionof anINITcommand. |
| 13    | Global Error             | 8192            | Aremoteinterfacehaserrorsintheerror queue.SY STem:E RRor?readsand deleteserrors.                                     |
| 14-15 | not used                 | not used        | 0isreturned                                                                                                          |

## StatusByte Register

This register summarizes the information from all other status groups as defined in the IEEE488.2 Standard Digital Interface for Programmable Instrumentation. The following table describes the bit assignments.

|   Bit | BitName                  | Decim alValue   | Defin ition                                                                                               |
|-------|--------------------------|-----------------|-----------------------------------------------------------------------------------------------------------|
|     0 | not used                 | not used        | 0isreturned                                                                                               |
|     1 | AlarmStatus Summary      | 2               | Oneor moreStatusAlarmconditionshaveoccurred.UseSTAT us:ALARm:E VENt?to readanddeleteerrors.               |
|     2 | Error Queue              | 4               | Oneor moreerrorsintheE rror Queue.SY STem:E RRor?readsanddeleteserrors.                                   |
|     3 | not used                 | not used        | 0isreturned                                                                                               |
|     4 | Message Available        | 16              | Dataisavailableintheinstrument'soutput buffer.                                                            |
|     5 | not used                 | not used        | 0isreturned                                                                                               |
|     6 | Master Status Summary    | 64              | Oneor morebitsareset intheStatusByteR egister andmaygenerateaService Request.Bitsmust beenabled,see*SR E. |
|     7 | OperationS tatus Summary | 128             | Oneor morebitsareset intheO perationStatusR egister.Bitsmust beenabled,see STATus:OPERation:ENABle.       |

## MSSBit

MSSisareal-time (unlatched) summary of all Status Byte register bits that are enabled by the Service Request Enable register. MSS is set whenever the instrument has one or more reasons for requesting service. *STB?reads the bits in the Status Byte register but does not clear them.

## Error and Output Queues

The Error Queue is a first-in, first-out (FIFO) data register that stores numerical and textual description of an error or event. Error messages are stored until they are read with SYSTem:ERRor? If the queue overflows, the last error/ event in the queue is replaced with error -350,"Queue overflow".

The Output Queue is a first-in, first-out (FIFO) data register that stores instrument-to-controller messagesuntil the controller reads them. Whenever the queue holds messages, it sets the MAV bit (4) of the Status Byte register.

## StatusDiagram

![Image](%20BT2152B-prg_artifacts/image_000075_d2e7001d851825c3e7972d01840826ac8b55f3529adc7a80a803c226c2be8ac9.png)

STATus:OPERation[:EVENt]?

## Reset and Interface Settings

Reset settings are applied when the unit is reset using the *RSTcommand.

| Param eter                          | Setting   |
|-------------------------------------|-----------|
| Over-current protection:            | 1.00e-2   |
| Over-voltageprotection:             | 4.0       |
| Under-voltageprotection:            | 3.0       |
| Output resistance:                  | 1.0       |
| Open-circuit voltage:               | 3.5       |
| Initia l cell current:              | 1.00e-3   |
| Test duration:                      | 5minutes  |
| Timeinterval <tint>:                | 1second   |
| Byteorder for binaryblocktransfers: | swapped   |
| Insitucurrent for wireresistance    | ±1mA      |
| Digital:O UTPut:Data                | set to0   |

Interface settings are the factory default settings (not affected by *RST).

| Param eter                               | Setting                                                   |
|------------------------------------------|-----------------------------------------------------------|
| LANinterface:                            | enabled                                                   |
| USBinterface:                            | enabled                                                   |
| DHCP:                                    | on                                                        |
| AutoIP:                                  | on                                                        |
| IPAddress:                               | 169.254.4.61                                              |
| Subnet Mask:                             | 255.255.0.0                                               |
| Default Gateway:                         | 0.0.0.0                                                   |
| DNSServer:                               | 0.0.0.0                                                   |
| Host Name:                               | K-BT 2152B-nnnnn( nnnnnislast 5digitsof theserial number) |
| LANServices:                             | all enabled                                               |
| Telnet prompt:                           | "BT 2152B>"                                               |
| IPaddressesof WindowsInternet NameSystem | 0.0.0.0                                                   |

Power must cycled for interface enable or LAN service changes to take effect. LAN settings changes require a LAN restart.

## SCPI Error Messages

- l Up to 20 errors can be stored in the error queue.
- l Aglobal error queue holds all power-on and hardware-related errors (example: over-temperature).
- l Error retrieval is first-in-first-out (FIFO), and errors are cleared as you read them. Once you have read all interface-specific errors, the errors in the global error queue are retrieved.
- l If more than 20 errors have occurred, the last error stored in the queue (the most recent error) is replaced with -350,"Error queue overflow". No additional errors are stored until you remove errors from the queue. If no errors have occurred when read, the instrument responds with +0,"No error".
- l Interface-specific error queues are cleared by power cycles or by *CLS. The error queue is not cleared by *RST.
- l The SYSTem:ERRor? query reads and clears one error from the error queue. Errors have the following format -113,"Undefined header". The error string may contain up to 255 characters.

## Error List

## Device-dependent Errors(these errors set Standard Event Status register bit #2)

201, "Memory lost: time and date";

Internal calibration time and date is lost

202, "Selftest failed";

The power-on self-test has failed

204, "NVRAM checksum error";

Anon-volatile RAM checksum error has occurred in the instrument

205, "NVRAM full";

The non-volatile RAM memory in the instrument is full

206, "File not found";

The internal calibration file was not found in NVRAM

207, "Power rail fault";

Oneor more of the internal power rails have failed

208, "Power supply fault";

Oneor more of the internal power supplies have failed

210, "diagnostic error";

An internal diagnostic error has occurred in the instrument

220, "data is not available";

4 Programming Reference

Measurement data is not available. No measurement readings have occurred

230, "External temperature sensor not connected.";

The external temperature sensor is not connected to the TEMPinput

231, "Internal temperature not within limits.";

The internal reference temperature is not within the specified limit

250, "Error during self-discharge measurement";

Aself-discharge measurement error has occurred. Error condition specific messages will be appended to this generic message.

260, "Analysis requires at least 2 channels in the channel list"

MEDian:FITand MEDian:SUBtraction commands require at least 2 channels for analysis.

270, "Readings not being collected";

Measurement readings are not being collected as the collection engine is not running.

271, "Not enough reading points collected";

Not enough reading points have been collected to return a measurement

309, "Incorrectly formatted channel list";

The channel list is incorrectly formatted. Check channel syntax - should be (@1:32) or similar.

316, "Mass storage error";

The mass storage memory has been exceeded

320, "Exceeded max number of licensed channels";

The command is specifying more channels than are supported by the installed license.

610, "Self Test Failure: Multiple errors during self test";

Multiple errors have occurred during self-test

611, "Self Test Failure: Voltage reference failed";

The internal reference voltage has failed during self-test.

612, "Self Test Failure: 10 mA Reference failed";

The internal 10 mA reference has failed during self-test.

613, "Self Test Failure: 100 mA Reference failed";

The internal 100 mA reference has failed during self-test.

680, "Incorrect cal password";

An incorrect calibration password has been entered

700, "Unknown calibration error occurred"; An unknown calibration error occurred 701, "Calibration has not been started."; The command used requires the instrument to be in calibration mode. 702, "The calibration result is out of the expected range."; The calibration value entered from the DVM is outside of the expected range 703, "Error during auto calibration."; An error has occurred during transfer calibration. Try running auto calibration again 800, "Nonvolatile memory write failure"; The instrument could not write to nonvolatile memory CommandErrors(these errorsset Standard Event Statusregister bit #2) -123, "Numeric overflow" The numeric value returned is larger than the expected value -203, "Command protected; instrument must be unsecured"; Calibration mode requires a password to unsecure the instrument -213, "INITignored"; The INIT:TESTcommand is ignored. There is already an init running. -221, "Settings conflict; invalid tint. "; Atest could not be executed because of invalid time interval parameter. -221, "Settings conflict; invalid test duration. "; Atest could not be executed because of invalid test duration parameter. -221, "Settings conflict; lower limit &gt; upper limit. "; Atest could not be executed because the lower limit is greater than the upper limit parameter. -221, "Settings conflict; cell open circuit voltage must be between over and under voltage. "; Atest did not execute because the open circuit voltage must be between the over and under voltage. -222, "Data out of range; value clipped to upper limit"; The measured data is out of range; the returned value is clipped to the upper limit. -222, "Data out of range; value clipped to lower limit"; The measured data is out of range; the returned value is clipped to the lower limit. -222, "Parameter 1 out of range";

## 4 Programming Reference

The command could not be executed because the 1st parameter is out of range.

-222, "Parameter 2 out of range";

The command could not be executed because the 2nd parameter is out of range.

-222, "Parameter 3 out of range";

The command could not be executed because the 3rd parameter is out of range.

-222, "Parameter 4 out of range";

The command could not be executed because the 4th parameter is out of range.

-222, "Parameter 5 out of range";

The command could not be executed because the 5th parameter is out of range.

-222, "Parameter 6 out of range";

The command could not be executed because the 6th parameter is out of range.

-222, "Parameter 7 out of range";

The command could not be executed because the 7th parameter is out of range.

-222, "Parameter 8 out of range";

The command could not be executed because the 8th parameter is out of range.

-222, "Parameter 9 out of range";

The command could not be executed because the 9th parameter is out of range.

-250, "Mass storage error; internal file system could not be opened";

The command could not be executed because the internal file system could not be opened

-250, "Mass storage error; USB file system could not be opened";

The command could not be executed because the USB file system could not be opened

-253, "Corrupt media; internal file system scan failed";

The command could not be executed because the internal file system scan failed

-253, "Corrupt media; internal file system format failed";

The command could not be executed because the internal file system format failed

- -253, "Corrupt media; file system corruption detected; reformat needed";

The command could not be executed because the internal file system is corrupted

-253, "Corrupt media; USB file system scan failed";

The command could not be executed because the USB file system scan failed

-350, "Error queue overflow";

The error queue is full. No additional errors can be stored until errors are removed from the queue.

![Image](%20BT2152B-prg_artifacts/image_000076_12a22d464d9a3558f59286fac10e7d1323b96785c70a9c4f1883ebb1dddfbf12.png)

## 5 Verification and Calibration

Verification Procedure

Reference Calibration

Channel Calibration

Wire Resistance Calibration

Calibration Security Reset

Maintenance

## Verification Procedure

## Introduction

Verification is recommended to verify that the instrument is working properly after receipt and unpacking. Verification is also recommended if you notice suspicious instrument behavior or if there is a question about the performance of the instrument. Verification procedures can be time consuming as they verify the operation of a single channel at a time.

![Image](%20BT2152B-prg_artifacts/image_000077_add61f570cc5d677ac7c338d2c6572c5b88b21c8cfbb225190b01f8ea6b4bccd.png)

Performing a reference calibration and a channel calibration provides the same high level of confidence as the manual channel-by-channel verification process.

Verification is not necessary as part of a standard maintenance cycle. It is also not necessary after performing any of the calibration procedures, as the calibration processes verify that the reference and channels are functioning within specification.

Verification commands set each channel to a specific output level, which can then be used to verify the specified accuracy of the channel at that operating point. If the instrument fails any of the verification tests, try performing the Reference and Channel calibrations again. If verification is still unsuccessful, return the unit to a Keysight Technologies Service Center.

## Verification Equipment and Considerations

- l A7½-digit DMM, Keysight 34470A (Run auto-calibration on the DMM prior to starting)
- l BT2152-60002 Verification kit - for BT2152A
- l BT2183AVerification fixture - for BT2152B
- l The ambient temperature is stable and between 20 °Cand 28 °C.Relative humidity is &lt;80%
- l The BT2152A/B must be warmed up for at least 1 hour prior to verification tests

## Verification Fixtures

Amulti-channel breakout board assembly can simplify verification when planning to verify all channels. This can be constructed by wiring all BT2152A/B channels in parallel at the breakout board. Only one channel at a time can be tested with this arrangement. When selected, that channel is electrically connected. The remaining channels have internal switches keeping them disconnected

## Verification Kit - for BT2152A

The Keysight BT2152-60002 verification kit includes the following parts:

- l 1 - Verification fixture (see below) p/ n BT2152-65510
- l 8 - Ethernet Cat6A, 26AWG, 8-conductor, 1ft. cables p/ n 8121-3032

Connect the eight Ethernet cables to the verification fixture and to the back of the BT2152A. Connect the inputs of the 7½-digit DMM, for voltage or current verification to the banana plugs on the verification kit. A user-supplied banana-plug cable is recommended.

![Image](%20BT2152B-prg_artifacts/image_000078_6a33d32fe5f43d825a3e92844c68f9c25e39dfa4826602283f0cce60db92a707.png)

## Verification Fixture - for BT2152B

Connect the Keysight BT2183A verification fixture directly into the two 37-pin D subminiature connectors on the back of the BT2152B. Connect the inputs of the 7½-digit DMM, for voltage or current verification to the banana plugs on the verification fixture. A user-supplied banana-plug cable is recommended. You do not need to provide a 442-ohm resistor for current verification, as it is included on the fixture.

![Image](%20BT2152B-prg_artifacts/image_000079_9588119935b5bd46db1c5e94e933a62cb81b70572cf701541c507b2ffd448eaa.png)

## Zero-Scale Current Accuracy Verification

Verifying the measurement system at zero, the bottom of the range, verifies contribution due to offset errors in the system. A significant consideration here is verifying the extremely low + 1 µA offset specification of BT2152A/B's current measurement system. Noise inherent in the BT2152A/B's output typically requires a 1-minute measurement integration time be used with the DMM to average the noise out down to a + 1 µA level. However, this can be circumvented by testing the channel at zero by using an open circuit. For this reason, the BT2152A/B's zero-scale current measurement is verified prior to making any connection to any channel.

The zero-scale current measurement accuracy procedure is a s follows:

![Image](%20BT2152B-prg_artifacts/image_000080_c9f0192e8c497a14ada9423ba4b1ae662ed9f9b3472f60e3856633c5c1963f93.png)

No channel connections are required for the zero-scale current accuracy verification.

Step 1. Start the verification. Send CAL:VER:STAR&lt;channel&gt;

| Verification Step 1        |   Setting |
|----------------------------|-----------|
| Select thechannel toverify |         1 |

Step 2. Wait 15 seconds for the unit to settle before proceeding with measurements

Step 3. Start the zero-scale current verification. Send CAL:VER:MEAS:INIT &lt;time&gt;, &lt;tint&gt;. The front panel TESTlight flashes orange when this command is executed.

| Verification Step 3                      | Setting   |
|------------------------------------------|-----------|
| Set thetimefor themeasurement inseconds  | <time>=10 |
| Set theinterval themeasurement inseconds | <tint>=10 |

Step 4. Wait for the measurement time set in step 3 to complete. Either send SENS:VER:AVAI? until the query returns a "1", or wait until the front panel TESTlight turns off.

Step 5. Fetch the measurement reading from the BT2152A/B. Send FETC:CURR:LAT? (@chanlist)

| Verification Step 5                   | Setting   |
|---------------------------------------|-----------|
| Returnthemeasurement datafromachannel | @1        |

Step 6. Verify that the zero-scale current error is within the specified accuracy provided in the Quick Reference section of this guide.

Step 7. If verifying multiple channels, repeat steps 1 through 7 for the rest of the channels.

Step 8. End the zero-scale current verification. Send CAL:VER:END

## Full-Scale Current Accuracy Verification

Current measurement accuracy is verified near or at the 10-mA full-range current. Gain error is significant at the top of the range and adds to any offset error in the system. The fixture incorporates a 442 ohm resistor. During full-scale current accuracy verification this resistor is in series between the DMMmeasuring current and the output channel, to establish the current level at near or at 10 mA for verification.

Step 1. If you have not already done so, connect a 7.5 digit (or better) DMM to the verification fixture.

Step 2. Set the DMM for DCcurrent measurement, 10 mA range, and 10 PLCs (to integrate noise).

Step 3. Start the verification. Send CAL:VER:STAR&lt;channel&gt;

| Verification Step 3        |   Setting |
|----------------------------|-----------|
| Select thechannel toverify |         1 |

Step 4. Set an output voltage. Send CAL:VER:VOLT&lt;voltage&gt;

Step 5. Wait 15 seconds for the BT2152A/B to settle before proceeding with measurements.

| Verification Step 4                                                                                      | Setting       |
|----------------------------------------------------------------------------------------------------------|---------------|
| Set thetop-endcurrent measurement range.(4.5V providesapproximately10mAwiththe442-ohm resistor inplace.) | <voltage>=4.5 |

Step 6. Initiate a measurement. Send CAL:VER:MEAS:INIT&lt;time&gt;, &lt;tint&gt;. The front panel TESTlight flashes orange when this command is executed.

| Verification Step 6                      | Setting   |
|------------------------------------------|-----------|
| Set thetimefor themeasurement inseconds  | <time>=10 |
| Set theinterval themeasurement inseconds | <tint>=10 |

Step 7. While the BT2152A/B is performing its measurements, take a current reading with the DMM and record this value.

Step 8. Wait for the measurement time set in step 6 to complete. Either send SENS:VER:AVAI? until the query returns a "1", or wait until the front panel TESTlight turns off.

Step 9. Fetch the measurement reading from the BT2152A/B. Send FETC:CURR:LAT? (@chanlist)

| Verification Step 9                   | Setting   |
|---------------------------------------|-----------|
| Returnthemeasurement datafromachannel | @1        |

Step 10. Subtract the reference reading from the DMM obtained in step 7 from the reading from the BT2152A/Bmeasurement obtained in step 9. Verify if it within the specified accuracy provided in the Quick Reference section of this guide.

Step 11. If verifying multiple channels, repeat steps 3 through 10 for the remainder of the channels in the BT2152A/B.

Step 12. End the current verification. Send CAL:VER:END

## Voltage Accuracy Verification

The voltage measurement accuracy is verified near or at the top and bottom of the scale. Offset error dominates at the bottom of the scale while gain error becomes significant at the top of the scale.

Step 1. Leave the DMM connected to the verification fixture.

Step 2. Set the DMM for DCvoltage measurement, 10 V range, and 10 PLCs (to integrate noise).

Step 3. Start the verification. Send CAL:VER:STAR&lt;channel&gt;

| Verification Step 3        |   Setting |
|----------------------------|-----------|
| Select thechannel toverify |         1 |

5 Verification and Calibration

Step 4. Set an output voltage. Send CAL:VER:VOLT&lt;voltage&gt;

| Verification Step 4                       | Setting       |
|-------------------------------------------|---------------|
| Set thebottom-endmeasurement rangevoltage | <voltage>=0.5 |

Step 5. Wait 15 seconds for the BT2152A/B to settle before proceeding with measurements.

Step 6. Initiate a measurement. Send CAL:VER:MEAS:INIT&lt;time&gt;, &lt;tint&gt;. The front panel TESTlight flashes orange when this command is executed.

| Verification Step 6                      | Setting   |
|------------------------------------------|-----------|
| Set thetimefor themeasurement inseconds  | <time>=10 |
| Set theinterval themeasurement inseconds | <tint>=10 |

Step 7. While the BT2152A/B is performing its measurements, take a voltage reading with the DMM and record this value.

- Step 8. Wait for the measurement time set in step 6 to complete. Either send SENS:VER:AVAI? until the query returns a "1", or wait until the front panel TESTlight turns off.
- Step 10. Subtract the reference reading from the DMM obtained in step 7 from the reading from the BT2152A/Bmeasurement obtained in step 9. Verify if it within the specified accuracy provided in the Quick Reference section of this guide.
- Step 11. Repeat steps 4 through 10 with the voltage set to 4.5 V, to test the top end of the voltage measurement scale.
- Step 12. If verifying multiple channels, repeat steps 3 through 11 for the remainder of the channels in the BT2152A/B.

Step 9. Fetch the measurement reading from the BT2152A/B. Send FETC:VOLT:LAT? (@chanlist)

| Verification Step 9                   | Setting   |
|---------------------------------------|-----------|
| Returnthemeasurement datafromachannel | @1        |

Step 13. End the voltage verification. Send CAL:VER:END

## Reference Calibration

## Introduction

The instrument features closed-case electronic calibration; no internal mechanical adjustments are required. The instrument calculates correction factors based on reference values that you enter and stores correction factors in non-volatile memory until the next calibration is performed.

## Calibration Interval

The instrument should be calibrated on a regular interval as determined by the maintenance schedule.

## Calibration Considerations

- l The following equipment is recommended for calibration: 7½-digit DMM; Keysight 34470A (Run auto-calibration on the DMM prior to starting the reference calibration)
- l The calibration ambient temperature is stable and between 20 °Cand 28 °C.Relative humidity is &lt;80%.
- l If set, the correct password is required to enter calibration mode. The password is factory-set to 0 (zero). You can change the password once calibration mode is entered to prevent unauthorized access to the calibration mode (See CALibration:SECure:CODE).
- l You can calibrate any one of the four calibrations steps independently of the other steps and then store those results. The other existing calibration values will not be affected.
- l Awarm up time of 1 hour is required before the unit can be calibrated.

## External DMM Connectionsand Setup

The following figure illustrates the connections between the CAL connector on the rear panel of the BT2152A/B and the DMM. Twisted interconnect wires of minimum length are recommended between the instrument and the DMM to reduce settling and noise errors.

Step 1. Connect a 7.5 digit (or better) DMM to the calibration connector using three wires, twisted together, according to the pin-out shown in the previous figure.

![Image](%20BT2152B-prg_artifacts/image_000081_e7ea613d9b3a7bd531bb92b62f1e0e5c54600ed8153d1eda8bd166c0ab5f7038.png)

5 Verification and Calibration

Step 2. Power-on the DMM and allow it to warm-up, as required.

Step 3. Plug the connector into the Cal port on the rear of the BT2152A/B to be calibrated.

## Enter Calibration Mode

The following SCPI command starts the calibration. It aborts any other instrument process that is running and prepares the instrument for reference calibration.

Send CAL:STAR

The front panel Test light flashes orange when calibration is running. The Test light turns off when calibration is complete.

## Voltage Calibration

Step 1. Put the DMM in voltage measurement mode in AUTOrange, with a minimum of 100 PLC averaging, auto input impedance (not 10M).

Step 2. Start the voltage calibration for channel 4. Send CAL:STEP 1

Step 3. Trigger a voltage measurement on the DMM. Measure the voltage between V and Com.

| Cal Step 1               | Calibration Limits   |
|--------------------------|----------------------|
| Beginsvoltagecalibration | 3.3Vto3.8V           |

Step 4. Send the valid measurement to the instrument. Send CAL:RES? &lt;value&gt;

Step 5. Start the voltage offset calibration for channel 4. Send CAL:STEP 2

Step 6. Trigger a voltage measurement on the DMM. Measure the voltage between V and Com.

| Cal Step 2                       | Calibration Limits   |
|----------------------------------|----------------------|
| Beginsvoltageoffset calibra tion | -0.001Vto0.001V      |

Step 7. Send the valid measurement to the instrument. Send CAL:RES? &lt;value&gt;

![Image](%20BT2152B-prg_artifacts/image_000082_108ac7c8180d29c59834babab738f97d30d73d098ff293b789e263d1ee630d25.png)

If CAL:RES? returns a value other than zero (0), an error has occurred. Send SYST:ERR? to return the error. Check the calibration setup; then re-run the step.

## Current Calibration

- Step 1. Put the DMM in current measurement mode on the 10 mA range with a minimum of 100 PLC averaging. Make sure the DMM's current input terminal is connected to cal port pin 3 as shown in the previous figure.

Step 2. Start the 10 mA current calibration for channel 4. Send CAL:STEP 3,4

Step 3. Trigger a current measurement on the DMM. Measure the current between Com and I.

| Cal Step 3                     | Calibration Limits   |
|--------------------------------|----------------------|
| Begins10mAcurrent calibra tion | 0.008Ato0.011A       |

## Step 4. Send the valid measurement to the instrument. Send CAL:RES? &lt;value&gt;

![Image](%20BT2152B-prg_artifacts/image_000083_23a50544d2185961d61f93684819d928b0da87261831bfb1e47c2190bb483507.png)

If CAL:RES? returns a value other than zero (0), an error has occurred. Send SYST:ERR? to return the error. Check the calibration setup; then re-run the step.

## End Calibration and Store Results

Step 1. End calibration. This returns the instrument to the *RST/ Power-on state and sets the CAL:STEP to 0. Send CAL:END

Step 2. Store the calibration results. This step overwrites the previous calibration constants. Send CAL:STOR

Step 3. Disconnect the DMM from the instrument.

## Channel Calibration

![Image](%20BT2152B-prg_artifacts/image_000084_d4d95bbee433da06dfbb2cded4137e59829fe55c8b685c80ee460ce423fc70a6.png)

IMPORTANT Remove all connections from the CAL connector on the rear panel of the BT2152A/B before performing the transfer calibration.

Channels should be calibrated on a regular interval as determined by the maintenance schedule. During channel calibration, each individual channel is sequentially connected to the internal reference and gain and offset corrections are calculated and stored in non-volatile memory.

## Prerequisites

- l The unit must pass self-test, which is run at the start of channel calibration. If self-test (*TST?) does not pass, channel calibration (*CAL?) will abort.
- l The unit must be warmed up. A warm up time of 1 hour is required before the unit can be calibrated. The front panel Ready light must be green, otherwise *CAL? will abort.
- l The unit must stay within its temperature limits. If the unit exceeds the limits, *CAL? will abort.

## Running Channel Calibration

Send *CAL?

This calibration is automatic and takes up to 1 hour.

The front panel Test light flashes orange when channel calibration is running. The Test light turns off when calibration is complete.

## If Problems Occur with Channel Calibration

If the calibration value of a specific channel is out of the accepted tolerance, that channel will fail. The remaining channels will continue to calibrate, with the calibration results being stored when calibration completes.

An error will be placed in the error queue with the channel number that failed, along with measurement information detailing the issue. Use SYSTem:ERRor? to read the error queue. See SCPI Error Messages for more information.

## Aborting Channel Calibration

If you need to abort channel calibration, either press the Stop button on the front panel for one second, or send a device clear.

The Test light turns off when channel calibration stops.

![Image](%20BT2152B-prg_artifacts/image_000085_c3b6fbfcb4457d4ddc9330f31802bbc06d68519787e124e9e55049dbff1c5e8a.png)

You can also query the status register using a different connection and check when the cal bit returns to 0. If you are using the LAN interface for example, you can query the status register using the USB interface.

## Wire Resistance Calibration

## Benefits of Wire Resistance Calibration

The Keysight BT2152A/B Self-Discharge Analyzer can measure and compensate for cable resistance with the wire resistance calibration procedure. Wire resistance should be calibrated using In Situ calibration before every self-discharge test. If this is not feasible, wire resistance should be calibrated on a regular interval as determined by the maintenance schedule.

- l Using wire resistance calibration lets you run discharge measurements with better performance when using programmable resistance, because the cable wiring will be taken into account.
- l Wire resistance calibration values only apply to the probes and wires in place when the calibration was performed. If the contact probes change and/or the cell cables on the instrument end are unplugged, reinserted, or reseated, the wiring resistance calibration function should be performed again.
- l After running wire resistance calibration and saving the values, you can query the present resistance values using the SENS:WIRE:RES:CONF? (@&lt;chanlist&gt;) query. If you have previously saved wire resistance values to non-volatile memory, you can now compare the present values to the previous values. This method lets you capture any resistance drifts over time. When the contact resistances of a specific channel/ cell probe becomes too high (indicating overuse) the probe and/ or wire should be replaced.

NOTE

To query the previously saved resistance values, you must first load them into the instrument using CAL:WIRE:RES:LOAD &lt;1|2|3|4|5&gt; . As this overwrites the present values, you will need to save the present values before you load any previous values.

Refer to Programmable wire resistance accuracy for information on wire resistance calibration performance over the supported range of 0 Ω to 5 Ω .

## In situ Calibration Procedure

In situ calibration lets you calibrate the wires and probes while connected to the cells being tested. This has the benefits of calibration in place with no external shorting bars or external instruments. It also is the best method to account for probe contact resistance, as the probes are in contact with the cells during the calibration procedure - with wire ends still connected to the cells.

In situ wire resistance calibration is preferred over external DMM calibration methods as it provides optimal performance and takes less time.

Step 1. Makesureall cell cables are installed at the back of the BT2152A/B .

Step 2. Enter the appropriate test current of the LI cells using CONF:INS:CURRHIGH|MED|LOW. The default setting (LOW) will disturb the cells the least and should be appropriate for most cells.

Step 3. Specify the channels that you will be calibrating and start the wire resistance calibration procedure by sending CAL:WIRE:RES:INS (@&lt;chanlist&gt;).

5 Verification and Calibration

Step 4. Watch the front panel Test light. It flashes orange when wire resistance calibration is running, and turns off when calibration is complete (in about 2 minutes or so). If you are not near the front panel, query the instrument using SENS:WIRE:RES:AVAI? until the instrument returns a 1.

Step 5. Check the error queue to make sure there are no errors using SYST:ERR? Errors would indicate a cell was not present at the end of the cable.

Step 6. Optional - Save the resistance values found to non-volatile memory using CAL:WIRE:RES:SAVE&lt;1|2|3|4|5&gt;.

## By-short Calibration Procedure

By-short calibration requires you to short the probes together during the calibration procedure. The cells must be disconnected and replaced by a metal shorting bar during the calibration procedure. This method does not adequately account for the actual probe contact resistance when the probes are in contact with the cells. By-short calibration is included for backward compatibility with previous versions of the BT2152A. For best results, in situ calibration is the recommended calibration procedure.

In situ wire resistance calibration is preferred over the by-short or external DMM calibration methods as it provides optimal performance and takes less time.

Step 1. Makesureall cell cables are installed at the back of the BT2152A/B.

Step 2. Disconnect all cellsfrom the cell cablesand short the endsof the cell cablestogether. .

Step 3. If you are using the BT2152A/B to make and enter the resistance measurement, short the ends of each wire-pair that would normally be connected to the cell together. Otherwise you must use an external DMM to measure the resistance across the wire ends.

Skip steps 4 - 7 if you are using an external DMM.

Step 4. To start the wire resistance calibration procedure, send CAL:WIRE:RES:AUTO

Step 5. Watch the front panel Test light. It flashes orange when wire resistance calibration is running, and turns off when calibration is complete (in about 20 minutes). If you are not near the front panel, query the instrument using SENS:WIRE:RES:AVAI? until the instrument returns a 1.

Step 6. Check the error queue to make sure there are no errors using SYST:ERR? Errors would indicate a cell was not disconnected, or a low resistance short was not detected at the end of the cable.

Step 7. Optional - Save the resistance values found to non-volatile memory using CAL:WIRE:RES:SAVE&lt;1|2|3|4|5&gt;.

Steps 8 and 9 only apply if you are using an external DMM to make resistance measurements.

Step 8. Measure the resistances of each cell cable pair using an external DMM and record the results..

Step 9. Enter the results into the BT2152A/B using the SENS:WIRE:RES:CONF&lt;value&gt;, (@&lt;chanlist&gt;) command.

Step 10. Removetheshortsat the end of the cable wires and reconnect the wires to the LI cells.

## Calibration Security Reset

![Image](%20BT2152B-prg_artifacts/image_000086_cb12cfc2b73ab4cc70b07f739931fd8d2cad3d245576e8c45aeb427287b4e3c3.png)

SHOCKHAZARDOnlyqualified, service-trained personnel whoare aware of the hazards involved should remove covers. Alwaysdisconnect external power before servicing.

## Electrostatic Discharge (ESD) Precautions

Almost all electrical components can be damaged by electrostatic discharge (ESD) during handling. Component damage can occur at electrostatic discharge voltages as low as 50 V.

The following guidelines will help prevent ESD damage during service operations:

- l Disassemble instruments only in a static-free work area.
- l Use a conductive work area to reduce static charges.
- l Use a conductive wrist strap to reduce static charge accumulation.
- l Remove all plastic, foam, vinyl, paper, and other static-generating materials from the immediate work area.

## ToolsRequired

- l T10 Torx driver - for cover removal
- l Clip leads - for shorting connector pins

## Cover Removal

1. Turn off the power. Remove all cables from the instrument.
2. Remove the 6 flat-head screws located on the top and the 7 pan-head screws along the sides (see below). Place the screws in a container so that you do not lose them.

![Image](%20BT2152B-prg_artifacts/image_000087_15eced2e5fa549917e0ac912d67ba253aec5d80e444740e93c9f498176eeb2b7.png)

3. Remove the instrument cover.

## Password Reset

1. Locate the controller PC board in the right rear corner of the instrument (as viewed from the back of the unit).
2. On the controller board, locate connector P701. Short pins A6 to pin B6 as shown in the red rectangle.
3. Turn the instrument ON, allow it to boot-up, wait 3 minutes, then turn the instrument OFF again.
4. Remove the short from pins A6/B6.
5. Reassemble the cover.
6. Turn the unit on. The security code will now be reset to the default value of 0 (zero).

![Image](%20BT2152B-prg_artifacts/image_000088_f5e4b6248726de38a248043b85017afb0e26c347016295c2ff7e82030a7e51a1.png)

## Maintenance

The following table describes the maintenance tasks for the Keysight BT2152A/B as well as their recommended frequency.

| Maintenance Task                 | Recommended Schedule                                                                              |
|----------------------------------|---------------------------------------------------------------------------------------------------|
| ReferenceC alibra tion           | Runannually(onceper year).                                                                        |
| Channel Calibration              | Runafter Referencecalibration.                                                                    |
|                                  | AND                                                                                               |
|                                  | Runmonthly,or duringanyproductionlinedowntime(e.g.scheduledmaintenance).                          |
| WireResistancecalibration        | RuntheInsituwirecalibrationbeforeeveryself dischargemeasurement,andafter servicing.               |
|                                  | If youcannot useInsitumethodandmust useby-short method,runtheby-short after Channel calibra tion. |
|                                  | AND                                                                                               |
|                                  | Runafter thecell fixturehasbeenchangedor replaced.                                                |
|                                  | AND                                                                                               |
|                                  | Runafter thecell fixturewiringischangedor unplugged.                                              |
| Individual channel verifica tion | Not part of aregular maintenanceschedule.                                                         |
|                                  | Theseteststhat arerecommendedasanacceptancetest whenyoufirst receivetheinstrument or if you       |
|                                  | feel thereissomequestionabout theperformanceof theinstrument (i.e , suspiciousbehavior).          |
|                                  | Alternatively, areferencecalibrationandchannel calibrationwouldgivethesamehighlevel of            |
|                                  | confidenceasthemanual channel verificationprocess.                                                |

Index Running a test 62 retrieving values 63 stopping 64

|                         | Digital Commands 77                   | Introduction 58     |
|-------------------------|---------------------------------------|---------------------|
|                         | Digital Port 38                       | SCPI Language 58    |
| A                       | Fault 40                              |                     |
| Air flow 17, 25         | I/O 38                                | K                   |
| B                       | Inhibit 40                            | Keywords 58         |
| By-short 128            | Input 39                              | L                   |
| C                       | E                                     | LEDdescription 13   |
| Calibration 123         | Environment 25                        | LXI command 89      |
| channel 126             | Error messages 111                    | M                   |
| interval 123            | External Temperature Meas- urement 17 | Maintenance 131     |
| security reset 129      |                                       | O                   |
| wire resistance 127     | F                                     | OUTPut command 90   |
| Calibration Commands 66 | Factory Reset 111                     |                     |
| Cell Stability 51       | Fetch Commands 79                     | P                   |
| Channel parameter 59    | FIFO 111                              | Parameter Types 59  |
| Cleaning 10             | First-in-first-out 111                | power-on 36         |
| Clear Status 111        | FORMat command 86                     | Programming         |
| CLS 111                 | Front Panel Operation 36              | samples 62          |
| Common Commands 72      | G                                     | protection event 37 |
| 76                      |                                       |                     |
| CONFigurecommand        | GPIB 111                              | Q                   |
| Connections             | I                                     | Queries 59          |
| cell cables 29          | I/O 111                               | Queue 111           |
| interface 27            |                                       | I/O 111             |
| power cord 26           | queue 111                             | Quick Reference 18  |
| Contacting              | In situ 127                           |                     |
| Keysight 12             | INITiatecommands 87                   | R                   |
| D Device Clear 61       | Inspect 24                            | Reset settings 110  |

clearing protection 64 S Safety 25 notices 9 symbols 8 SCPI 58 SCPI Language 58 introduction 58 Sense Commands 91 Specifications 15 STATus 93 Status System Diagram 109 Status Tutorial 105 Subsystem commands 65 Syntax Conventions 59 System Commands 97 V Verification 118