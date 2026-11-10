---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.7 AccountDetails <AcctDtls>", "24.4.8.16 SettlementPartiesDetails <SttlmPtiesDtls>", "24.4.8.16.3 SecuritiesSettlementSystemIdentification <SctiesSttlmSysId>"]
file_pages: [506]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.8.16.3 SecuritiesSettlementSystemIdentification <SctiesSttlmSysId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 506 to 506.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 506

```text
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition30Choice" on page 5255 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5255
Or}   Proprietary <Prtry> [1..1] ± 5255
24.4.8.16.3  SecuritiesSettlementSystemIdentification <SctiesSttlmSysId>
Presence: [0..1]
Definition: Identification of a specific system or set of rules and/or processes to be applied at the
settlement place.
Datatype: "Max35Text" on page 5403
24.4.8.16.4  ReceivingSideDetails <RcvgSdDtls>
Presence: [0..1]
Definition: Chain of receiving settlement parties.
Impacted by: C7 "BookTransferGuideline", C11 "DepositoryGuideline", C25 "Party2PresenceRule", C26
"Party3PresenceRule", C27 "Party4PresenceRule", C28 "Party5PresenceRule", C32
"SettlementChainGuideline"
ReceivingSideDetails <RcvgSdDtls> contains the following SettlementParties131 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 507
   Party1 <Pty1> [0..1] ± 508
   Party2 <Pty2> [0..1] ± 508
   Party3 <Pty3> [0..1] ± 509
   Party4 <Pty4> [0..1] ± 509
   Party5 <Pty5> [0..1] ± 510
Constraints
• BookTransferGuideline
In the case of an own account internal transfer, the account of (delivering) Party2 at (delivering)
Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
• DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 506 May 2026
```

