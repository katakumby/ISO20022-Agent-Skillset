---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["3 camt.065.001.01 LimitUtilisationJournalReportV01"]
file_pages: [9]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 3 camt.065.001.01 LimitUtilisationJournalReportV01

Source: [src-000363](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 9 to 9.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 9

```text
3 camt.065.001.01
LimitUtilisationJournalReportV01
3.1 MessageDefinition Functionality
The LimitUtilisationJournalReport message is exchanged between the central system and a central
securities depository or a directly connected system party (the central securities depository participant
granted direct access, like a bank or central counter party) and is used to return information about the
limit. Its purpose is to report information regarding the journal of transactions impacting the utilisation of
limits that have been defined by the system participant.
Outline
The LimitUtilisationJournalReportV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Set of elements used to provide information on the header of the message.
B. Pagination
Pagination of the message.
Usage: the pagination of the message is only allowed when agreed between the parties.
C. ReportOrError
Provides information on report or error resulting from the originating query message.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 9 February 2025
```

