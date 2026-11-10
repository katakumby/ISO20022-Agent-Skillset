---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>", "53.4.5.16.3 FinancialInstrumentQuantityChoice <FinInstrmQtyChc>", "53.4.5.16.3.5 DigitalTokenUnit <DgtlTknUnit>"]
file_pages: [3560]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16.3.5 DigitalTokenUnit <DgtlTknUnit>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3560 to 3560.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3560

```text
53.4.5.16.3.5  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
53.4.5.16.3.6  HoldingsRedemptionRate <HldgsRedRate>
Presence: [1..1]
Definition: Portion of the investor's holdings to be redeemed.
Datatype: "PercentageRate" on page 5401
53.4.5.16.4  InvestmentAccountDetails <InvstmtAcctDtls>
Presence: [0..1]
Definition: Account impacted by the investment fund order.
Impacted by: C26 "OrderOriginatorEligibility2Rule"
InvestmentAccountDetails <InvstmtAcctDtls> contains the following InvestmentAccount81
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 3560
   AccountName <AcctNm> [0..1] Text 3560
   AccountDesignation <AcctDsgnt> [0..1] Text 3561
   OwnerIdentification <OwnrId> [0..*] ± 3561
   AccountServicer <AcctSvcr> [0..1] ± 3561
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3561
   SubAccountDetails <SubAcctDtls> [0..1] ± 3562
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3562
Constraints
• OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
53.4.5.16.4.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
53.4.5.16.4.2  AccountName <AcctNm>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3560 May 2026
```

