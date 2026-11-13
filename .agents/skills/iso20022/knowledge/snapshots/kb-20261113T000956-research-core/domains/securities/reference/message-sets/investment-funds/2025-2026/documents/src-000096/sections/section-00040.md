---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["4 acmt.003.001.08 AccountModificationInstructionV08", "4.4 Message Building Blocks", "4.4.7 ModifiedIntermediaries <ModfdIntrmies>"]
file_pages: [70]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.003.001.08"]
---

# 4.4.7 ModifiedIntermediaries <ModfdIntrmies>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 70 to 70.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 70

```text
SecondaryOwner/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
Beneficiary/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet)
PowerOfAttorney/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
LegalGuardian/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet)
SuccessorOnDeath/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
Administrator/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet)
OtherParty/OtherPartyDetails/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
Granter/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet)
Settlor/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet)
SeniorManagingOfficial/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
Protector/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet).
4.4.7 ModifiedIntermediaries <ModfdIntrmies>
Presence: [0..*]
Definition: Information related to intermediaries to be inserted, updated or deleted.
ModifiedIntermediaries <ModfdIntrmies> contains the following elements (see
"ModificationScope40" on page 4963 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4963
   Intermediary <Intrmy> [1..1] ± 4963
4.4.8 ModifiedPlacement <ModfdPlcmnt>
Presence: [0..1]
Definition: Information related to referral information to be inserted, updated or deleted.
ModifiedPlacement <ModfdPlcmnt> contains the following elements (see "ModificationScope43" on
page 4923 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4924
   Placement <Plcmnt> [1..1] ± C30 4924
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 70 May 2026
```

