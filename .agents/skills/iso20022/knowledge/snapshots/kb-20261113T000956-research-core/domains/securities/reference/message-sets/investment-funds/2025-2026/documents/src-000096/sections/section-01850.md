---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.16 TransactionOverhead <TxOvrhd>", "47.4.4.8.16.3 IndividualTax <IndvTax>", "47.4.4.8.16.3.1 Type <Tp>"]
file_pages: [2601, 2602]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.16.3.1 Type <Tp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2601 to 2602.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2601

```text
IndividualTax <IndvTax> contains the following Tax42 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  2601
{Or     Code <Cd> [1..1] CodeSet 2601
Or}     Proprietary <Prtry> [1..1] ± 2603
   Tax <Tax> [0..1]  2603
{Or     Amount <Amt> [1..1] Amount C3, C10 2603
Or}     Rate <Rate> [1..1] Rate 2604
   Country <Ctry> [0..1] CodeSet C8 2604
   ExemptionIndicator <XmptnInd> [1..1] Indicator 2604
   ExemptionReason <XmptnRsn> [0..1]  2604
{Or     Code <Cd> [1..1] CodeSet 2604
Or}     Proprietary <Prtry> [1..1] ± 2607
   RecipientIdentification <RcptId> [0..1] ± 2607
   TaxCalculationDetails <TaxClctnDtls> [0..1]  2608
     Basis <Bsis> [1..1]  2608
{Or       Code <Cd> [1..1] CodeSet 2608
Or}       Proprietary <Prtry> [1..1] ± 2608
47.4.4.8.16.3.1  Type <Tp>
Presence: [1..1]
Definition: Type of tax.
Type <Tp> contains one of the following TaxType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2601
Or}   Proprietary <Prtry> [1..1] ± 2603
47.4.4.8.16.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of tax expressed as a code.
Datatype: "TaxType17Code" on page 5375
CodeName Name Definition
PROV Provincial Tax is a provincial tax.
NATI NationalTax Tax is a national tax.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2601 May 2026
```

## File page 2602

```text
CodeName Name Definition
STAT StateTax Tax is a state tax.
WITH WithholdingTax Tax is on income deducted at source,
which the paying agent is legally obliged
to deduct from its payments of interest
on deposits and other proceeds of a
financial instrument.
KAPA CapitalGainTax Tax is on a capital gain (realised and
unrealised), that is, the profit that is
gained from the sale of a financial
instrument.
NKAP CapitalLossCredit Tax recovery is due to capital loss.
INPO InterimProfitTax Tax is on the sum of all earnings/
revenues accrued since the last dividend
distribution.
STAM StampDuty Tax is on certain documents and
transactions.
WTAX WealthTax Tax is a special tax imposed, applicable
only when the value of assets or
categories of assets owned by an entity
are above a given ceiling defined by the
tax authority. Wealth tax is not linked to
income.
INHT InheritanceTax Tax that is payable at the time of death
on any items (money or otherwise),
where ownership changes either upon
death or within a legally specified
number of years before death.
SOSU SolidaritySurcharge Tax that is levied by legal authorities for
solidarity purposes.
CTAX TaxCredit Direct reduction of an individual's tax
liability.
GIFT GiftTax Tax that is levied on assets given to
individuals prior to the death of the
donor. Gift tax is designed to ensure the
integrity of the inheritance tax,
preventing the pre-death transfer of
wealth.
COAX ConsumptionTax Tax that is levied on goods and services
purchased by customers, and is added
to the retail price.
EUTR EUTaxRetention Tax withheld at source in the framework
of the European Directive on taxation of
savings in the form of interest payments.
AKT1 Aktiengewinn1 Share-related profit. This is a tax specific
to the German market. The share-
related-profit gives the fund the
opportunity to pass on to the institutional
investor redeeming fund units certain
tax-free income from equity. The
calculation method is based on the old
Investment Tax Act
(Investmentsteuergesetz).
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2602 May 2026
```

