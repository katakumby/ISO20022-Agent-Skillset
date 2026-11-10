---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.7 InvestmentAccountDetails <InvstmtAcctDtls>"]
file_pages: [3041]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.7 InvestmentAccountDetails <InvstmtAcctDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3041 to 3041.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3041

```text
50.4.4.7  InvestmentAccountDetails <InvstmtAcctDtls>
Presence: [1..1]
Definition: Account impacted by the investment fund order.
Impacted by: C25 "OrderOriginatorEligibility2Rule"
InvestmentAccountDetails <InvstmtAcctDtls> contains the following InvestmentAccount81
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 3041
   AccountName <AcctNm> [0..1] Text 3041
   AccountDesignation <AcctDsgnt> [0..1] Text 3041
   OwnerIdentification <OwnrId> [0..*] ± 3042
   AccountServicer <AcctSvcr> [0..1] ± 3042
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3042
   SubAccountDetails <SubAcctDtls> [0..1] ± 3042
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3043
Constraints
• OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
50.4.4.7.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
50.4.4.7.2  AccountName <AcctNm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
50.4.4.7.3  AccountDesignation <AcctDsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to reconciled
individually.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3041 May 2026
```

