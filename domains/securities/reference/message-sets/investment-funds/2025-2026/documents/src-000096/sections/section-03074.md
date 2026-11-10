---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "64.4 Message Building Blocks", "64.4.3 IndividualOrderConfirmationDetailsReport <IndvOrdrConfDtlsRpt>", "64.4.3.8 InvestmentAccountDetails <InvstmtAcctDtls>"]
file_pages: [4293]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.057.001.03"]
---

# 64.4.3.8 InvestmentAccountDetails <InvstmtAcctDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4293 to 4293.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4293

```text
Definition: Party that initiates the status of the order confirmation.
StatusInitiator <StsInitr> contains the following elements (see "PartyIdentification139" on page 5043
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
64.4.3.8  InvestmentAccountDetails <InvstmtAcctDtls>
Presence: [0..1]
Definition: Account information of the individual order confirmation for which the status is given.
Impacted by: C6 "OrderOriginatorEligibility2Rule"
InvestmentAccountDetails <InvstmtAcctDtls> contains the following InvestmentAccount81
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 4293
   AccountName <AcctNm> [0..1] Text 4293
   AccountDesignation <AcctDsgnt> [0..1] Text 4294
   OwnerIdentification <OwnrId> [0..*] ± 4294
   AccountServicer <AcctSvcr> [0..1] ± 4294
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 4294
   SubAccountDetails <SubAcctDtls> [0..1] ± 4295
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 4295
Constraints
• OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
64.4.3.8.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
64.4.3.8.2  AccountName <AcctNm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4293 May 2026
```

