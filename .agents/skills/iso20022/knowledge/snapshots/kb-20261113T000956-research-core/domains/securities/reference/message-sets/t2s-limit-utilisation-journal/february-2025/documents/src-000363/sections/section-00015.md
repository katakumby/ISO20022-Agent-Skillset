---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["3 camt.065.001.01 LimitUtilisationJournalReportV01", "3.4 Message Building Blocks", "3.4.3 ReportOrError <RptOrErr>", "3.4.3.1 BusinessReport <BizRpt>", "3.4.3.1.1 LimitIdentification <LmtId>"]
file_pages: [17]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 3.4.3.1.1 LimitIdentification <LmtId>

Source: [src-000363](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 17 to 17.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 17

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         Code <Cd> [1..1] CodeSet 26
Or}         Proprietary <Prtry> [1..1] Text 26
       Description <Desc> [0..1] Text 27
3.4.3.1.1  LimitIdentification <LmtId>
Presence: [1..1]
Definition: Identification of the limit on which information is requested.
LimitIdentification <LmtId> contains the following LimitIdentification7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] ± 17
   Type <Tp> [1..1] CodeSet 17
   LimitCurrency <LmtCcy> [0..1] CodeSet C1 18
   AccountOwner <AcctOwnr> [1..1] ± 18
   BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 18
3.4.3.1.1.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique identification as assigned by the account servicer to unambiguously identify the
account.
AccountIdentification <AcctId> contains one of the following elements (see
"AccountIdentification4Choice" on page 30 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C4 30
Or}   Other <Othr> [1..1] ± 30
3.4.3.1.1.2  Type <Tp>
Presence: [1..1]
Definition: Nature of the risk management limit.
Datatype: "LimitType4Code" on page 42
CodeName Name Definition
EXGT ExternalGuarantee Limit is related to a cap amount granted
by a national central bank or a
settlement bank.
UCDT UnsecuredCredit Limit is related to a cap amount granted
by a national central bank or a
settlement bank, but generally
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 17 February 2025
```

