---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.21 PhysicalDeliveryIndicator <PhysDlvryInd>"]
file_pages: [3914]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.21 PhysicalDeliveryIndicator <PhysDlvryInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3914 to 3914.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3914

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
55.4.5.19.21  PhysicalDeliveryIndicator <PhysDlvryInd>
Presence: [1..1]
Definition: Indicates whether the financial instrument is to be physically delivered.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
55.4.5.19.22  PhysicalDeliveryDetails <PhysDlvryDtls>
Presence: [0..1]
Definition: Information related to the physical delivery of the securities.
PhysicalDeliveryDetails <PhysDlvryDtls> contains the following elements (see
"DeliveryParameters3" on page 5096 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Address <Adr> [1..1] ± 5096
   IssuedCertificateNumber <IssdCertNb> [0..1] Text 5097
55.4.5.19.23  DigitalAssetSettlement <DgtlAsstSttlm>
Presence: [0..1]
Definition: Total quantity of digital asset to be paid or received in exchange for the securities token.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3914 May 2026
```

