---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09", "21.3 Constraints"]
file_pages: [711, 712]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.027.001.09"]
topic_continuations: [{"constraint_ids": ["C23", "C24", "C25", "C26"], "until_heading": "21.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 713, "topic": "21.3 Constraints", "reference_path": "domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00465.md"}]
---

# 21.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 711 to 712.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 21.3 Constraints topic continues in [Constraints continuation C23–C26 (file p713)](section-00465.md#file-page-713). Read the text before **21.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 711

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     SettlementDate <SttlmDt> [1..1] ± 723
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C15,
C16,
C17,
C18
723
     ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C15,
C16,
C17,
C18
724
     Investor <Invstr> [0..1] ± 725
   SupplementaryData <SplmtryData> [0..*] ± C26 726
21.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C4 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C5 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C6 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C7 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 711 March 2026
```

## File page 712

```text
C8 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C9 DescriptionUsageRule
Description must be used alone as the last resort.
C10 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C11 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C12 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C13 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be
NONREF.
C14 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C15 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C16 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C17 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C18 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C19 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C20 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C21 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C22 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 712 March 2026
```

