---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.17 SubscriptionLegDetails <SbcptLegDtls>", "53.4.5.17.3 FinancialInstrumentQuantityChoice <FinInstrmQtyChc>", "53.4.5.17.3.5 DigitalTokenUnit <DgtlTknUnit>"]
file_pages: [3629]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.17.3.5 DigitalTokenUnit <DgtlTknUnit>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3629 to 3629.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3629

```text
53.4.5.17.3.5  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
53.4.5.17.4  InvestmentAccountDetails <InvstmtAcctDtls>
Presence: [0..1]
Definition: Account impacted by the investment fund order.
Impacted by: C26 "OrderOriginatorEligibility2Rule"
InvestmentAccountDetails <InvstmtAcctDtls> contains the following InvestmentAccount81
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 3629
   AccountName <AcctNm> [0..1] Text 3629
   AccountDesignation <AcctDsgnt> [0..1] Text 3630
   OwnerIdentification <OwnrId> [0..*] ± 3630
   AccountServicer <AcctSvcr> [0..1] ± 3630
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3630
   SubAccountDetails <SubAcctDtls> [0..1] ± 3631
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3631
Constraints
• OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
53.4.5.17.4.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
53.4.5.17.4.2  AccountName <AcctNm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3629 May 2026
```

