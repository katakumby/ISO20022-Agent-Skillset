---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.26 TransactionOverhead <TxOvrhd>", "49.4.5.9.26.5 IndividualFee <IndvFee>", "49.4.5.9.26.5.1 Type <Tp>", "49.4.5.9.26.5.1.2 Proprietary <Prtry>"]
file_pages: [2840]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.26.5.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2840 to 2840.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2840

```text
CodeName Name Definition
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
49.4.5.9.26.5.1.2  Proprietary <Prtry>
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
49.4.5.9.26.5.2  Basis <Bsis>
Presence: [0..1]
Definition: Method used to calculate the fee (charge/commission).
Basis <Bsis> contains one of the following ChargeBasis2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2840
Or}   Proprietary <Prtry> [1..1] ± 2841
49.4.5.9.26.5.2.1  Code <Cd>
Presence: [1..1]
Definition: Fee (charge/commission) basis expressed as a code.
Datatype: "TaxationBasis5Code" on page 5366
CodeName Name Definition
FLAT Flat Charge/tax basis is a lump sum.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2840 May 2026
```

