---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.8 Charge", "66.1.8.1 Fees2", "66.1.8.1.2 IndividualFee <IndvFee>", "66.1.8.1.2.1 Type <Tp>", "66.1.8.1.2.1.2 Proprietary <Prtry>"]
file_pages: [4437]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.8.1.2.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4437 to 4437.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4437

```text
CodeName Name Definition
FEND FrontEndLoad Fee paid by the investor to the fund or
fund management company when
subscribing.
TRAN TransferFee In investment funds, a fee charged for
the transfer of ownership of an
investment fund.
POST PostageCharge Charge paid for the postage.
REGF RegulatoryFee Fee charged by a regulatory authority,
for example, securities and exchange
fees.
SHIP ShippingCharge Charge for shipping, including the
insurance of securities.
SPCN SpecialConcessions Fees, drawdown, or other reduction from
or in addition to the deal price.
66.1.8.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of fee expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.8.1.2.2  Basis <Bsis>
Presence: [0..1]
Definition: Method used to calculate the fee.
Basis <Bsis> contains one of the following ChargeBasis2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4437
Or}   Proprietary <Prtry> [1..1] ± 4438
66.1.8.1.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Fee (charge/commission) basis expressed as a code.
Datatype: "TaxationBasis5Code" on page 5366
CodeName Name Definition
FLAT Flat Charge/tax basis is a lump sum.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4437 May 2026
```

