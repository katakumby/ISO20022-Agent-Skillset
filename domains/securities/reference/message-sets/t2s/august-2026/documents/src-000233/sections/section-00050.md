---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["6 camt.065.001.01 LimitUtilisationJournalReportV01", "6.4 Message Building Blocks", "6.4.3 ReportOrError <RptOrErr>", "6.4.3.1 BusinessReport <BizRpt>", "6.4.3.1.2 LimitReport <LmtRpt>", "6.4.3.1.2.1 LimitJournal <LmtJrnl>", "6.4.3.1.2.1.1 Limit <Lmt>", "6.4.3.1.2.1.1.1 Amount <Amt>"]
file_pages: [86]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 6.4.3.1.2.1.1.1 Amount <Amt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 86 to 86.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 86

```text
Limit <Lmt> contains the following LimitAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1]  86
     Amount <Amt> [1..1] ± 86
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 86
   UtilisationAmount <UtlstnAmt> [1..1]  87
     Amount <Amt> [1..1] ± 87
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 87
   AvailableAmount <AvlblAmt> [1..1]  87
     Amount <Amt> [1..1] ± 87
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 88
6.4.3.1.2.1.1.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money of the limit, expressed in an eligible currency.
Amount <Amt> contains the following CreditDebitAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 86
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 86
6.4.3.1.2.1.1.1.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money expressed in an eligible currency.
Amount <Amt> contains one of the following elements (see "Amount2Choice" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 2840
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 2841
6.4.3.1.2.1.1.1.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Specifies whether the amount of money is a debit or a credit.
Datatype: "CreditDebitCode" on page 3234
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities 86 August 2026
```

