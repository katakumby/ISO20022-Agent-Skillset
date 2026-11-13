---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.18 RelatedQuantities <RltdQties>"]
file_pages: [211]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.18 RelatedQuantities <RltdQties>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 211 to 211.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 211

```text
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 886
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
2.4.2.15.18.2.18  RelatedQuantities <RltdQties>
Presence: [0..*]
Definition: Set of elements used to identify the related quantities, such as securities, in the underlying
transaction.
RelatedQuantities <RltdQties> contains one of the following TransactionQuantities4Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C10 211
Or   OriginalAndCurrentFaceAmount
<OrgnlAndCurFaceAmt>
[1..1] ± 212
Or}   Proprietary <Prtry> [1..1]  212
     Type <Tp> [1..1] Text 212
     Quantity <Qty> [1..1] Text 212
2.4.2.15.18.2.18.1  Quantity <Qty>
Presence: [1..1]
Definition: Specifies the quantity (such as securities) in the underlying transaction.
Impacted by: C10 "DigitalTokenUnitUsageRule"
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity33Choice" on
page 880 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 880
Or   FaceAmount <FaceAmt> [1..1] Amount 880
Or   AmortisedValue <AmtsdVal> [1..1] Amount 881
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 881
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
211 March 2026
```

