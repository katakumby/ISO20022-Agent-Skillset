---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.41 Service Level Agreement", "66.1.41.1 ModificationScope44", "66.1.41.1.1 ModificationScopeIndication <ModScpIndctn>"]
file_pages: [5144]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.41.1.1 ModificationScopeIndication <ModScpIndctn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5144 to 5144.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5144

```text
66.1.41.1.1  ModificationScopeIndication <ModScpIndctn>
Presence: [1..1]
Definition: Specifies the type of modification to be applied.
Datatype: "DataModification1Code" on page 5293
CodeName Name Definition
INSE InsertNewDataSet Insert a new set of data.
UPDT UpdateDataSetDetails Update the details of an existing set of
data.
DELT DeleteDataSet Delete an existing set of data.
66.1.41.1.2  ServiceLevelAgreement <SvcLvlAgrmt>
Presence: [1..1]
Definition: Identification of information which is part of a service level agreement.
ServiceLevelAgreement <SvcLvlAgrmt> contains the following elements (see "DocumentToSend4"
on page 5144 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 5144
   Recipient <Rcpt> [1..1] ± 5145
   MethodOfTransmission <MtdOfTrnsmssn> [1..1]  5145
{Or     Code <Cd> [1..1] CodeSet 5145
Or}     Proprietary <Prtry> [1..1] ± 5145
66.1.41.2  DocumentToSend4
Definition: Type of document and the type of communication method to be used to notify a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 5144
   Recipient <Rcpt> [1..1] ± 5145
   MethodOfTransmission <MtdOfTrnsmssn> [1..1]  5145
{Or     Code <Cd> [1..1] CodeSet 5145
Or}     Proprietary <Prtry> [1..1] ± 5145
66.1.41.2.1  Type <Tp>
Presence: [1..1]
Definition: Type of document.
Datatype: "Max140Text" on page 5402
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5144 May 2026
```

