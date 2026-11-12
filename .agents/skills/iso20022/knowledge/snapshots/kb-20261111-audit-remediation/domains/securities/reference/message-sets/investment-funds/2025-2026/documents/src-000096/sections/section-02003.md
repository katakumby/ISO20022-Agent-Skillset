---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.5 OrderType <OrdrTp>"]
file_pages: [2825]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.5 OrderType <OrdrTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2825 to 2825.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2825

```text
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 5403
49.4.5.9.5  OrderType <OrdrTp>
Presence: [0..10]
Definition: Category of the investment fund order.
OrderType <OrdrTp> contains one of the following elements (see "FundOrderType4Choice" on
page 4740 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4741
Or}   Proprietary <Prtry> [1..1] ± 4741
49.4.5.9.6  InvestmentAccountDetails <InvstmtAcctDtls>
Presence: [1..1]
Definition: Account impacted by the investment fund order execution.
Impacted by: C25 "OrderOriginatorEligibility2Rule"
InvestmentAccountDetails <InvstmtAcctDtls> contains the following InvestmentAccount81
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 2825
   AccountName <AcctNm> [0..1] Text 2826
   AccountDesignation <AcctDsgnt> [0..1] Text 2826
   OwnerIdentification <OwnrId> [0..*] ± 2826
   AccountServicer <AcctSvcr> [0..1] ± 2826
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 2826
   SubAccountDetails <SubAcctDtls> [0..1] ± 2827
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2827
Constraints
• OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
49.4.5.9.6.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2825 May 2026
```

