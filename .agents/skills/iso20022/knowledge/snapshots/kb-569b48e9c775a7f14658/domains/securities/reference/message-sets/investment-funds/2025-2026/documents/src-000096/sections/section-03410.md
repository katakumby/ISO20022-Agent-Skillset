---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.14 InvestmentAccount75", "66.1.24.14.22 AccountUsageType <AcctUsgTp>"]
file_pages: [4656]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.14.22 AccountUsageType <AcctUsgTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4656 to 4656.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4656

```text
BlockedStatus <BlckdSts> contains one of the following elements (see
"BlockedStatusReason2Choice" on page 5164 for details)
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
66.1.24.14.22  AccountUsageType <AcctUsgTp>
Presence: [0..1]
Definition: Specifies the type of usage of the account.
AccountUsageType <AcctUsgTp> contains one of the following elements (see
"AccountUsageType2Choice" on page 4555 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4555
Or}   Proprietary <Prtry> [1..1] ± 4555
66.1.24.14.23  ForeignStatusCertification <FrgnStsCertfctn>
Presence: [0..1]
Definition: Specifies if documentary evidence has been provided for the foreign resident.
Datatype: "Provided1Code" on page 5345
CodeName Name Definition
NPRO NotProvided Not provided.
PROV Provided Provided.
66.1.24.14.24  AccountSignatureDateTime <AcctSgntrDtTm>
Presence: [0..1]
Definition: Date the investor or account owner signs the open account form.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4656 May 2026
```

