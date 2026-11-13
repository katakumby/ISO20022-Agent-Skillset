---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.44 Statement Update Type", "66.1.44.1 StatementUpdateTypeCodeAndDSSCodeChoice", "66.1.44.1.2 StatementUpdateTypeAsDSS <StmtUpdTpAsDSS>"]
file_pages: [5164]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.44.1.2 StatementUpdateTypeAsDSS <StmtUpdTpAsDSS>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5164 to 5164.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5164

```text
Datatype: "StatementUpdateTypeCode" on page 5365
CodeName Name Definition
COMP Complete Statement is complete.
DELT Delta Statement contains changes only.
66.1.44.1.2  StatementUpdateTypeAsDSS <StmtUpdTpAsDSS>
Presence: [1..1]
Definition: Update type expressed as a data source scheme and a code used within the data source
scheme.
StatementUpdateTypeAsDSS <StmtUpdTpAsDSS> contains the following elements (see
"GenericIdentification7" on page 4538 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [1..1] Text 4539
   Information <Inf> [1..1] Text 4539
66.1.45 Status
66.1.45.1  BlockedStatusReason2Choice
Definition: Choice of formats for a blocked status reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5164
Or}   Reason <Rsn> [1..*]  5165
     TransactionType <TxTp> [1..1]  5165
{Or       Code <Cd> [1..1] CodeSet 5165
Or}       Proprietary <Prtry> [1..1] ± 5167
     Blocked <Blckd> [1..1] Indicator 5167
     Reason <Rsn> [0..*]  5167
{Or       Code <Cd> [1..1] CodeSet 5167
Or}       Proprietary <Prtry> [1..1] ± 5168
     AdditionalInformation <AddtlInf> [1..1] Text 5168
66.1.45.1.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: There is no reason available or to report for the closed account status.
Datatype: "NoReasonCode" on page 5331
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5164 May 2026
```

