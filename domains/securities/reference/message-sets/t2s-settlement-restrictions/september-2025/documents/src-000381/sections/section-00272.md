---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.2 Message Datatypes", "9.2.2 CodeSet", "9.2.2.12 CountryCode"]
file_pages: [323]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.2.2.12 CountryCode

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 323 to 323.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 323

```text
CodeName Name Definition
SPLF StockSplit Increase in a corporation's number of
outstanding equities without any change
in the shareholder's equity or the
aggregate market value at the time of
the split. Equity price and nominal value
are reduced accordingly.
TREC TaxReclaim Event related to tax reclaim activities.
TEND Tender Offer made to holders by a third party,
requesting them to sell (tender) or
exchange their securities.
DLST TradingStatusDelisted Security is no longer able to comply with
the listing requirements of a stock
exchange and is removed from official
board quotation.
SUSP TradingStatusSuspended Trading in the security has been
suspended.
EXWA WarrantExercise Option offered to holders to buy (call
warrant) or to sell (put warrant) a specific
amount of stock, cash, or commodity, at
a predetermined price, during a
predetermined period of time (which
usually corresponds to the life of the
issue).
WTRC WithholdingTaxReliefCertification Certification process for withholding tax
reduction or exemption based on the tax
status of the holder.
WRTH Worthless Booking out of valueless securities.
ACCU Accumulation Funds related event in which the income
(for example accumulation units) that
accrues during an accounting period is
retained within the fund instead of being
paid away to investors. The retained
income is nonetheless deemed to have
been distributed to investors for tax
purposes.
MTNG SecuritiesHoldersMeeting Ordinary or annual or extraordinary or
special general meeting.
INFO Information Information provided by the issuer
having no accounting/financial impact on
the holder.
9.2.2.12  CountryCode
Definition: Code to identify a country, a dependency, or another area of particular geopolitical interest,
on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).
Type: CodeSet
Format
pattern [A-Z]{2,2}
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 323 September 2025
```

