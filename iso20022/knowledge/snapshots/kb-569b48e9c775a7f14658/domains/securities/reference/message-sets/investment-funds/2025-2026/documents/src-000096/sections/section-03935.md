---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.2 InformativeTax2", "66.1.47.2.5 IndividualTax <IndvTax>", "66.1.47.2.5.1 Type <Tp>", "66.1.47.2.5.1.1 Code <Cd>"]
file_pages: [5227]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.2.5.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5227 to 5227.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5227

```text
Type <Tp> contains one of the following TaxType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5227
Or}   Proprietary <Prtry> [1..1] ± 5228
66.1.47.2.5.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of tax expressed as a code.
Datatype: "TaxType17Code" on page 5375
CodeName Name Definition
PROV Provincial Tax is a provincial tax.
NATI NationalTax Tax is a national tax.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5227 May 2026
```

