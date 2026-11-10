---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["10 seev.038.001.09 CorporateActionNarrativeV09", "10.4 Message Building Blocks"]
file_pages: [694]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.038.001.09"]
---

# 10.4 Message Building Blocks

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 694 to 694.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 694

```text
C4 DescriptionUsageRule
Description must be used alone as the last resort.
C5 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C6 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C7 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C8 OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the structure and usage of the Official Corporate Action Event Reference
(COAF). Those recommendations are
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
C9 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C10 SafekeepingAccountOrBlockChainAddress1Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C11 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present then SafekeepingAccount must be absent.
C12 SafekeepingAccountOrBlockChainAddress3Rule
If SafekeepingAccount is present, then BlockChainAddressOrWallet must be absent.
C13 SafekeepingPlaceRule
The SafekeepingPlace is only to be used by global custodians that allow their clients to specify
where the securities are to be held, for example, in an ICSD account versus an account at the
local CSD.
C14 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
10.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
10.4.1 AccountDetails <AcctDtls>
Presence: [0..1]
Definition: General information about the safekeeping account and the account owner.
Approved by the Securities SEG on 27 January 2026 seev.038.001.09 CorporateActionNarrativeV09
Corporate Actions - Maintenance 2025 - 2026 694 February 2026
```

