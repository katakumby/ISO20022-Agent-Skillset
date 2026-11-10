---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["6 camt.065.001.01 LimitUtilisationJournalReportV01"]
file_pages: [73]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 6 camt.065.001.01 LimitUtilisationJournalReportV01

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 73 to 73.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 73

```text
6 camt.065.001.01
LimitUtilisationJournalReportV01
6.1 MessageDefinition Functionality
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities 73 August 2026
```

