---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.16 TransactionOverhead <TxOvrhd>", "50.4.4.9.16.2 IndividualFee <IndvFee>", "50.4.4.9.16.2.1 Type <Tp>", "50.4.4.9.16.2.1.2 Proprietary <Prtry>"]
file_pages: [3075]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.16.2.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3075 to 3075.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3075

```text
CodeName Name Definition
INIT InitialCharge Charge paid at the time of the first
subscription.
PREM Premium In investment funds, pre-arranged
addition to the trade amount based on
the published net asset value.
CHAR ServiceProvisionFee Fee paid by the investor to a distributor/
intermediary or other service provider for
the provision of financial services.
SWIT Switch In investment funds, charge related to a
switch transaction.
UCIC UCITSCommission Charges paid by the investor to the fund
company for subscription and
redemption orders.
COMM Commission Amount paid out by the fund to a third
party.
SHIP ShippingCharge Charge for shipping, including the
insurance of securities.
POST PostageCharge Charge paid for the postage.
CDPL CommissionDePlacement Amount of cash due to an intermediary
for selling a product, or services, to a
third party.
ADDF AdditionalFee Additional fee not covered by another
fee type.
REGF RegulatoryFee Fee charged by a regulatory authority,
for example, securities and exchange
fees.
PENA Penalty Fee charged to the investor for early
redemption of the fund.
NTWK NetworkFee Network fee assigned to a transaction on
a DLT network.
50.4.4.9.16.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Fee (charge/commission) expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
50.4.4.9.16.2.2  Basis <Bsis>
Presence: [0..1]
Definition: Method used to calculate the fee (charge/commission).
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3075 May 2026
```

