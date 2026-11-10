---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.4 Portfolio <Prtfl>", "38.4.15.4.1 TaxEfficientProduct <TaxEffcntPdct>", "38.4.15.4.1.9 BonusOrWithdrawal <BnsOrWdrwl>", "38.4.15.4.1.9.1 TypeOfAmount <TpOfAmt>"]
file_pages: [1352]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.4.1.9.1 TypeOfAmount <TpOfAmt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1352 to 1352.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1352

```text
38.4.15.4.1.9.1  TypeOfAmount <TpOfAmt>
Presence: [1..1]
Definition: Specifies whether the amount is the result of a bonus paid, a withdrawal or other kind of
amount.
TypeOfAmount <TpOfAmt> contains one of the following TypeOfAmount1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1352
Or}   Proprietary <Prtry> [1..1] ± 1352
38.4.15.4.1.9.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of amount expressed as a code.
Datatype: "TaxWrapperAmountType1Code" on page 5377
CodeName Name Definition
BONU Bonus Type of amount is a bonus, for example,
a government bonus.
WTHD Withdrawal Type of amount is a withdrawal, for
example, a withdrawal for a first time
residential purchase.
38.4.15.4.1.9.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of amount expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
38.4.15.4.1.9.2  Amount <Amt>
Presence: [0..1]
Definition: Amount of the bonus paid or the claimed amount. For example, a claimed amount for a
lifetime ISA (LISA) or a government bonus paid out.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 5269
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1352 May 2026
```

