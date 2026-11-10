---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 semt.015.001.10 IntraPositionMovementConfirmationV10", "6.3 Constraints"]
file_pages: [165, 166]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.015.001.10"]
---

# 6.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 165 to 166.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 165

```text
6.3 Constraints
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
C3 AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information
that can be provided in a structured field.
C4 AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
C5 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C6 BalanceFromToRule
The BalanceFrom/Type must be different from the BalanceTo/Type.
C7 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C8 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C11 DescriptionUsageRule
Description must be used alone as the last resort.
Approved by the Securities SEG on 27 January 2026 semt.015.001.10
IntraPositionMovementConfirmationV10
Settlement And Reconciliation - Maintenance 2025 - 2026 165 March 2026
```

## File page 166

```text
C12 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C13 EventTypeRule
The use of a specific corporate action event type code is allowed only if this specific event
triggers a securities movement as per the Event Interpretation Grid published by the Securities
Market Practice Group (SMPG).
The corporate action event indicator code OTHR must only be used in case no other corporate
action event code is appropriate.
The corporate action event indicator code CHAN must only be used in case no other corporate
action event code is appropriate and only for an event which relates to a change.
The corporate action event indicator code REDM must only be used when the redemption is
decided by the issuer and not by the holders.
C14 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C15 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C16 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C17 PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO
10383 Market Identifier Code (MIC) must be used.
C18 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
This constraint is defined at the MessageDefinition level.
C19 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
This constraint is defined at the MessageDefinition level.
C20 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
Approved by the Securities SEG on 27 January 2026 semt.015.001.10
IntraPositionMovementConfirmationV10
Settlement And Reconciliation - Maintenance 2025 - 2026 166 March 2026
```

