---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.4 InvestmentAccountDetails <InvstmtAcctDtls>", "41.4.4.8.4.1 AccountIdentification <AcctId>"]
file_pages: [1737]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.4.1 AccountIdentification <AcctId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1737 to 1737.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1737

```text
InvestmentAccountDetails <InvstmtAcctDtls> contains the following InvestmentAccount81
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 1737
   AccountName <AcctNm> [0..1] Text 1737
   AccountDesignation <AcctDsgnt> [0..1] Text 1737
   OwnerIdentification <OwnrId> [0..*] ± 1737
   AccountServicer <AcctSvcr> [0..1] ± 1738
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 1738
   SubAccountDetails <SubAcctDtls> [0..1] ± 1738
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1739
Constraints
• OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
41.4.4.8.4.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
41.4.4.8.4.2  AccountName <AcctNm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
41.4.4.8.4.3  AccountDesignation <AcctDsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to reconciled
individually.
Datatype: "Max35Text" on page 5403
41.4.4.8.4.4  OwnerIdentification <OwnrId>
Presence: [0..*]
Definition: Party that legally owns the account.
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1737 May 2026
```

