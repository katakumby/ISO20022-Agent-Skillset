---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.3 Constraints"]
file_pages: [669, 670]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.3 Constraints

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 669 to 670.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 669

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
   SubPayingAgent <SubPngAgt> [0..*] ± 690
   SupplementaryData <SplmtryData> [0..*] ± C23 690
9.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 AdditionalInformationRule
All elements in the AdditionalInformation sequence must not contain information that can be
provided in a structured field unless bilaterally agreed or advised differently in the element
definition as in AdditionalInformation/NarrativeVersion.
This constraint is defined at the MessageDefinition level.
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
C7 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C8 DescriptionUsageRule
Description must be used alone as the last resort.
C9 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 669 February 2026
```

## File page 670

```text
C10 EventTypeRule
If Code is present, the code OTHR (Other) must only be used in case no other corporate action
event code is appropriate.
If Code is present, the code CHAN (Change) must only be used in case no other corporate
action event code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM (Final Maturity) must only be used when the redemption is
decided by the issuer and not by the securities holders.
C11 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C12 IntermediateSecuritiesDistribution1Rule
If CorporateActionGeneralInformation/EventType/Code is RHDI
(IntermediateSecuritiesDistribution), then CorporateActionDetails/
IntermediateSecuritiesDistributionType must be present.
(MT 566 NVR C5).
On Condition
    /CorporateActionGeneralInformation/EventType/Code is equal to value 
'IntermediateSecuritiesDistribution'
Following Must be True
    /CorporateActionDetails Must be present
 And    /CorporateActionDetails/FollowingEventTypeIndicator Must be present
This constraint is defined at the MessageDefinition level.
C13 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C14 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C15 IssuerAgentGuideline
IssuerAgent must be used only in the communication between a CSD and local custodians.
This constraint is defined at the MessageDefinition level.
C16 OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the structure and usage of the Official Corporate Action Event Reference
(COAF). Those recommendations are
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
C17 OptionNumberRule
The CorporateActionConfirmationDetails/OptionNumber value provided must be the same as
the one provided in the related CorporateActionOptionDetails/OptionNumber element of the
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 670 February 2026
```

