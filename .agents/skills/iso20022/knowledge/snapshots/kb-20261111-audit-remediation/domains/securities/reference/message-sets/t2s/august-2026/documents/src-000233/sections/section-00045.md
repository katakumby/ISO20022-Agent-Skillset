---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["6 camt.065.001.01 LimitUtilisationJournalReportV01", "6.4 Message Building Blocks", "6.4.3 ReportOrError <RptOrErr>", "6.4.3.1 BusinessReport <BizRpt>", "6.4.3.1.1 LimitIdentification <LmtId>"]
file_pages: [81]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 6.4.3.1.1 LimitIdentification <LmtId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 81 to 81.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 81

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         Code <Cd> [1..1] CodeSet 90
Or}         Proprietary <Prtry> [1..1] Text 90
       Description <Desc> [0..1] Text 91
6.4.3.1.1  LimitIdentification <LmtId>
Presence: [1..1]
Definition: Identification of the limit on which information is requested.
LimitIdentification <LmtId> contains the following LimitIdentification7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] ± 81
   Type <Tp> [1..1] CodeSet 81
   LimitCurrency <LmtCcy> [0..1] CodeSet C1 82
   AccountOwner <AcctOwnr> [1..1] ± 82
   BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 82
6.4.3.1.1.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique identification as assigned by the account servicer to unambiguously identify the
account.
AccountIdentification <AcctId> contains one of the following elements (see
"AccountIdentification4Choice" on page 2836 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 2837
Or}   Other <Othr> [1..1] ± 2837
6.4.3.1.1.2  Type <Tp>
Presence: [1..1]
Definition: Nature of the risk management limit.
Datatype: "LimitType4Code" on page 3261
CodeName Name Definition
EXGT ExternalGuarantee Limit is related to a cap amount granted
by a national central bank or a
settlement bank.
UCDT UnsecuredCredit Limit is related to a cap amount granted
by a national central bank or a
settlement bank, but generally
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities 81 August 2026
```

