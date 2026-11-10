---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.8 InvestmentAccountDetails <InvstmtAcctDtls>"]
file_pages: [3873]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.8 InvestmentAccountDetails <InvstmtAcctDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3873 to 3873.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3873

```text
55.4.5.19.8  InvestmentAccountDetails <InvstmtAcctDtls>
Presence: [0..1]
Definition: Account impacted by the investment fund order execution.
Impacted by: C25 "OrderOriginatorEligibility2Rule"
InvestmentAccountDetails <InvstmtAcctDtls> contains the following InvestmentAccount81
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 3873
   AccountName <AcctNm> [0..1] Text 3873
   AccountDesignation <AcctDsgnt> [0..1] Text 3873
   OwnerIdentification <OwnrId> [0..*] ± 3874
   AccountServicer <AcctSvcr> [0..1] ± 3874
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3874
   SubAccountDetails <SubAcctDtls> [0..1] ± 3874
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3875
Constraints
• OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
55.4.5.19.8.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
55.4.5.19.8.2  AccountName <AcctNm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
55.4.5.19.8.3  AccountDesignation <AcctDsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to reconciled
individually.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3873 May 2026
```

