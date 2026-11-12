---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "58.4 Message Building Blocks", "58.4.2 RequestDetails <ReqDtls>", "58.4.2.3 OrderReference <OrdrRef>", "58.4.2.3.5 DealReference <DealRef>"]
file_pages: [4243]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.018.001.05"]
---

# 58.4.2.3.5 DealReference <DealRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4243 to 4243.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4243

```text
58.4.2.3.5  DealReference <DealRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the order execution, as assigned by the confirming
party.
Datatype: "Max35Text" on page 5403
58.4.2.3.6  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 5403
58.4.2.3.7  InvestmentAccountDetails <InvstmtAcctDtls>
Presence: [0..1]
Definition: Account information of the individual order instruction or individual order cancellation request
for which the status is requested.
Impacted by: C5 "OrderOriginatorEligibility2Rule"
InvestmentAccountDetails <InvstmtAcctDtls> contains the following InvestmentAccount81
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 4243
   AccountName <AcctNm> [0..1] Text 4244
   AccountDesignation <AcctDsgnt> [0..1] Text 4244
   OwnerIdentification <OwnrId> [0..*] ± 4244
   AccountServicer <AcctSvcr> [0..1] ± 4244
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 4244
   SubAccountDetails <SubAcctDtls> [0..1] ± 4245
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 4245
Constraints
• OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
58.4.2.3.7.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.018.001.05 RequestForOrderStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4243 May 2026
```

