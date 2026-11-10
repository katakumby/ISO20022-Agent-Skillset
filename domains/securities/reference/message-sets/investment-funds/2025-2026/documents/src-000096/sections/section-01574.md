---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.17 PhysicalDeliveryIndicator <PhysDlvryInd>"]
file_pages: [2203]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.17 PhysicalDeliveryIndicator <PhysDlvryInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2203 to 2203.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2203

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
44.4.4.9.17  PhysicalDeliveryIndicator <PhysDlvryInd>
Presence: [1..1]
Definition: Indicates whether the financial instrument is to be physically delivered.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
44.4.4.9.18  PhysicalDeliveryDetails <PhysDlvryDtls>
Presence: [0..1]
Definition: Information related to the physical delivery of the securities.
PhysicalDeliveryDetails <PhysDlvryDtls> contains the following elements (see
"DeliveryParameters3" on page 5096 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Address <Adr> [1..1] ± 5096
   IssuedCertificateNumber <IssdCertNb> [0..1] Text 5097
44.4.4.9.19  RequestedSettlementCurrency <ReqdSttlmCcy>
Presence: [0..1]
Definition: Currency requested for settlement of cash proceeds.
Impacted by: C3 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
44.4.4.9.20  RequestedNAVCurrency <ReqdNAVCcy>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2203 May 2026
```

