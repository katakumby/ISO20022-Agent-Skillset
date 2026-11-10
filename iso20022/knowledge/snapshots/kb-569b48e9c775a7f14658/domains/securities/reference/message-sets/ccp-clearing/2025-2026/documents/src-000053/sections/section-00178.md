---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["6 MX secl.005.001.02 MarginReportV02"]
file_pages: [232]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.005.001.02"]
---

# 6 MX secl.005.001.02 MarginReportV02

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 232 to 232.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 232

```text
6 MX secl.005.001.02
MarginReportV02
6.1 MessageDefinition Functionality
Scope
The MarginReport message is sent by the central counterparty (CCP) to a clearing member to report
on:
- the exposure resulting from the trade positions
- the value of the collateral held by the CCP (market value of this collateral) and
- the resulting difference representing the risk encountered by the CCP.
The message definition is intended for use with the ISO20022 Business Application Header.
Usage
There are four possibilities to report the above information. Indeed, the margin report may be structured
as follows:
- per clearing member: the report will only show the information for the clearing member, or
- per clearing member and per financial instrument: the report will show the information for the clearing
member, structured by security identification, or
- per clearing member and per non clearing member: the report will show the information for the
clearing member (that is for global clearing member only) structured by non clearing member(s), or
- per clearing member and per non clearing member and per security identification: the report will show
the information for the clearing member (global clearing member only) structured by non clearing
member(s) and by security identification.
Outline
The MarginReportV02 MessageDefinition is composed of 6 MessageBuildingBlocks:
A. ReportParameters
Provides parameters of the margin report such as the creation date and time, the report currency or
the calculation date and time.
B. Pagination
Page number of the message (within a report) and continuation indicator to indicate that the report
is to continue or that the message is the last page of the report.
C. ClearingMember
Provides the identification of the account owner, that is the clearing member (individual clearing
member or general clearing member).
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.005.001.02 MarginReportV02
March 2026 232
```

