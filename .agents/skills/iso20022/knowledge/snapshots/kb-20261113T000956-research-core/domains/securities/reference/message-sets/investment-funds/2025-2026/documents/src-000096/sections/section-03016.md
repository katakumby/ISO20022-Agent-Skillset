---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "57.4 Message Building Blocks", "57.4.3 StatusReport <StsRpt>", "57.4.3.2 IndividualCancellationStatusReport <IndvCxlStsRpt>", "57.4.3.2.8 InvestmentAccountDetails <InvstmtAcctDtls>"]
file_pages: [4222]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.017.001.05"]
---

# 57.4.3.2.8 InvestmentAccountDetails <InvstmtAcctDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4222 to 4222.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4222

```text
57.4.3.2.8  InvestmentAccountDetails <InvstmtAcctDtls>
Presence: [0..1]
Definition: Account information of the individual order cancellation for which the status is given.
Impacted by: C6 "OrderOriginatorEligibility2Rule"
InvestmentAccountDetails <InvstmtAcctDtls> contains the following InvestmentAccount81
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 4222
   AccountName <AcctNm> [0..1] Text 4222
   AccountDesignation <AcctDsgnt> [0..1] Text 4222
   OwnerIdentification <OwnrId> [0..*] ± 4223
   AccountServicer <AcctSvcr> [0..1] ± 4223
   OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 4223
   SubAccountDetails <SubAcctDtls> [0..1] ± 4223
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 4224
Constraints
• OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
57.4.3.2.8.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
57.4.3.2.8.2  AccountName <AcctNm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
57.4.3.2.8.3  AccountDesignation <AcctDsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to reconciled
individually.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4222 May 2026
```

