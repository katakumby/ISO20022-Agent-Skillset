---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.4 FinancialInstrument87", "66.1.18.4.9 BlockedHoldingDetails <BlckdHldgDtls>", "66.1.18.4.9.1 BlockedHolding <BlckdHldg>"]
file_pages: [4499]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.4.9.1 BlockedHolding <BlckdHldg>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4499 to 4499.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4499

```text
BlockedHoldingDetails <BlckdHldgDtls> contains the following BlockedHoldingDetails2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BlockedHolding <BlckdHldg> [1..1] CodeSet 4499
   PartialHoldingUnits <PrtlHldgUnits> [0..1] Quantity 4499
   HoldingCertificateNumber <HldgCertNb> [0..1] Text 4500
Constraints
• HoldingCertificateNumberRule
If BlockHolding is CERT (Certificate) then HoldingCertificateNumber is mandatory.
On Condition
    /BlockedHolding is equal to value 'Certificate'
Following Must be True
    /HoldingCertificateNumber Must be present
• PartialHoldingUnits1Rule
If BlockHolding is NPRH (NonPartialHolding) then PartialHoldingUnits must not be present.
On Condition
    /BlockedHolding is equal to value 'NonPartialHolding'
Following Must be True
    /PartialHoldingUnits Must be absent
• PartialHoldingUnits2Rule
If BlockHolding is PRTH (PartialHolding) then PartialHoldingUnits is mandatory.
On Condition
    /BlockedHolding is equal to value 'PartialHolding'
Following Must be True
    /PartialHoldingUnits Must be present
• PartialHoldingUnits3Rule
If BlockHolding is CERT (Certificate) then PartialHoldingUnits must not be present.
On Condition
    /BlockedHolding is equal to value 'Certificate'
Following Must be True
    /PartialHoldingUnits Must be absent
66.1.18.4.9.1  BlockedHolding <BlckdHldg>
Presence: [1..1]
Definition: Specifies how the blocked account holding is defined.
Datatype: "Holding1Code" on page 5309
CodeName Name Definition
CERT Certificate Certificate.
NPRH NonPartialHolding Non partial holding.
PRTH PartialHolding Partial holding.
66.1.18.4.9.2  PartialHoldingUnits <PrtlHldgUnits>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4499 May 2026
```

