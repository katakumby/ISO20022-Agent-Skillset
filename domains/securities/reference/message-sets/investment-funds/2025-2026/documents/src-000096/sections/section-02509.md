---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.4 OrderReference <OrdrRef>"]
file_pages: [3537]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.4 OrderReference <OrdrRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3537 to 3537.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3537

```text
53.4.5.4  OrderReference <OrdrRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the order, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
53.4.5.5  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the order. This reference can typically be
used in a hub scenario to give the reference of the order as assigned by the underlying client.
Datatype: "Max35Text" on page 5403
53.4.5.6  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 5403
53.4.5.7  InvestmentAccountDetails <InvstmtAcctDtls>
Presence: [0..1]
Definition: Account impacted by the investment fund order.
Impacted by: C26 "OrderOriginatorEligibility2Rule"
InvestmentAccountDetails <InvstmtAcctDtls> contains the following InvestmentAccount81
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 3538
   AccountName <AcctNm> [0..1] Text 3538
   AccountDesignation <AcctDsgnt> [0..1] Text 3538
   OwnerIdentification <OwnrId> [0..*] ± 3538
   AccountServicer <AcctSvcr> [0..1] ± 3538
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3539
   SubAccountDetails <SubAcctDtls> [0..1] ± 3539
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3539
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3537 May 2026
```

