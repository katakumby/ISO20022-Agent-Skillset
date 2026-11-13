---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>", "3.4.2.1.2 AccountOrError <AcctOrErr>", "3.4.2.1.2.1 Account <Acct>", "3.4.2.1.2.1.9 CurrentBilateralLimit <CurBilLmt>"]
file_pages: [71]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1.2.1.9 CurrentBilateralLimit <CurBilLmt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 71 to 71.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 71

```text
MultilateralBalance <MulBal> contains the following elements (see "CashBalance13" on page 796 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount 796
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 797
   Type <Tp> [0..1]  797
{Or     Code <Cd> [1..1] CodeSet 797
Or}     Proprietary <Prtry> [1..1] Text 797
   Status <Sts> [0..1] CodeSet 797
   ValueDate <ValDt> [0..1] ± 797
   ProcessingDate <PrcgDt> [0..1] ± 798
   NumberOfPayments <NbOfPmts> [0..1] Quantity 798
   RestrictionType <RstrctnTp> [0..1]  798
     Type <Tp> [1..1] ± 798
     Description <Desc> [0..1] Text 799
     ProcessingType <PrcgTp> [0..1]  799
{Or       Code <Cd> [1..1] CodeSet 799
Or}       Proprietary <Prtry> [1..1] Text 800
3.4.2.1.2.1.9  CurrentBilateralLimit <CurBilLmt>
Presence: [0..*]
Definition: Limit fixed by a party A with regard to a specific counterparty B and corresponding to the
maximum amount of traffic that party A may send to party B. The bilateral limit can be expressed as a
debit limit or a credit limit.
With the help of a bilateral limit, the direct participant restricts the use of liquidity when clearing
payments with another direct participant.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 71 February 2025
```

