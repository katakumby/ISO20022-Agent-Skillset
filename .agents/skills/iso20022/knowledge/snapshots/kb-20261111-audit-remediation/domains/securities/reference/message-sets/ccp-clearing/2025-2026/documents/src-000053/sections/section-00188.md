---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["7 MX secl.006.001.02 DefaultFundContributionReportV02"]
file_pages: [246]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.006.001.02"]
---

# 7 MX secl.006.001.02 DefaultFundContributionReportV02

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 246 to 246.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 246

```text
7 MX secl.006.001.02
DefaultFundContributionReportV02
7.1 MessageDefinition Functionality
Scope
The DefaultFundContributionReport message is sent by the central counterparty (CCP) to a Clearing
member to report on the calculation of the default fund contribution and the potential net excess or
deficit.
The message definition is intended for use with the ISO20022 Business Application Header.
Usage
CCPs require participants to post assets in a clearing fund that can be used in the event of a default by
a participant, to compensate non-defaulting participants for losses they suffer due to this default. The
CCP evaluates each participant risk level based on their positions (monthly or daily) and calculate the
excess of deficit of the default fund contribution. The DefaultFundContributionReport is usually sent on
a monthly basis.
Outline
The DefaultFundContributionReportV02 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. ReportParameters
Provides details about the report such as the report identification, the calculation date, the value
date.
B. ClearingMember
Provides the identification of the account owner, that is the clearing member (individual clearing
member or general clearing member).
C. ReportDetails
Provides details on the default fund report.
D. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.006.001.02
DefaultFundContributionReportV02
March 2026 246
```

