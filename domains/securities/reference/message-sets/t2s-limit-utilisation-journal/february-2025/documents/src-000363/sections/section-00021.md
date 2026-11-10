---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["3 camt.065.001.01 LimitUtilisationJournalReportV01", "3.4 Message Building Blocks", "3.4.3 ReportOrError <RptOrErr>", "3.4.3.1 BusinessReport <BizRpt>", "3.4.3.1.2 LimitReport <LmtRpt>", "3.4.3.1.2.1 LimitJournal <LmtJrnl>", "3.4.3.1.2.1.1 Limit <Lmt>", "3.4.3.1.2.1.1.2 UtilisationAmount <UtlstnAmt>"]
file_pages: [23]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 3.4.3.1.2.1.1.2 UtilisationAmount <UtlstnAmt>

Source: [src-000363](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 23 to 23.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 23

```text
3.4.3.1.2.1.1.2  UtilisationAmount <UtlstnAmt>
Presence: [1..1]
Definition: Utilised amount of money of the limit expressed in an eligible currency.
UtilisationAmount <UtlstnAmt> contains the following CreditDebitAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 23
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 23
3.4.3.1.2.1.1.2.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money expressed in an eligible currency.
Amount <Amt> contains one of the following elements (see "Amount2Choice" on page 31 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 31
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 31
3.4.3.1.2.1.1.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Specifies whether the amount of money is a debit or a credit.
Datatype: "CreditDebitCode" on page 42
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
3.4.3.1.2.1.1.3  AvailableAmount <AvlblAmt>
Presence: [1..1]
Definition: Remaining amount of money of the limit expressed in an eligible currency.
AvailableAmount <AvlblAmt> contains the following CreditDebitAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 23
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 24
3.4.3.1.2.1.1.3.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money expressed in an eligible currency.
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 23 February 2025
```

