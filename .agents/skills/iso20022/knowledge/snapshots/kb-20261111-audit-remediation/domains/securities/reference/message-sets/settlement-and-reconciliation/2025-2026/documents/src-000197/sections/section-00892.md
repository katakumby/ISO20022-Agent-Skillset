---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06", "34.4 Message Building Blocks"]
file_pages: [1326]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.040.001.06"]
preceding_topic_continuations: [{"constraint_ids": ["C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22"], "until_heading": "34.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 1326, "topic": "34.3 Constraints", "reference_path": "domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00891.md"}]
---

# 34.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1326 to 1326.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 1326, C9–C22 before **34.4 Message Building Blocks** continue [34.3 Constraints](section-00891.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 1326

```text
C9 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C10 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C11 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C12 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C13 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C14 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C15 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C16 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C17 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C18 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C19 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C20 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C21 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C22 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
34.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities SEG on 27 January 2026 sese.040.001.06
SecuritiesSettlementTransactionCounterpartyRespo
nseV06
Settlement And Reconciliation - Maintenance 2025 - 2026 1326 March 2026
```

