---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["3 acmt.002.001.08 AccountDetailsConfirmationV08", "3.4 Message Building Blocks", "3.4.8 Placement <Plcmnt>"]
file_pages: [50]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.002.001.08"]
---

# 3.4.8 Placement <Plcmnt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 50 to 50.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 50

```text
Intermediaries <Intrmies> contains the following elements (see "Intermediary46" on page 5023 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  5023
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C4 5024
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 5024
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 5024
   Account <Acct> [0..1]  5024
     Identification <Id> [0..1] Text 5025
     AccountServicer <AcctSvcr> [1..1] ± 5025
   WaivedTrailerCommissionIndicator <WvdTrlrComssnInd> [0..1] Indicator 5025
   Role <Role> [0..1] ± 5025
   PrimaryCommunicationAddress <PmryComAdr> [0..*] ± 5025
   SecondaryCommunicationAddress <ScndryComAdr> [0..*] ± 5026
   NameAndAddress <NmAndAdr> [0..1] ± 5026
3.4.8 Placement <Plcmnt>
Presence: [0..1]
Definition: Confirmation of referral information.
Impacted by: C30 "ReferredPlacementAgentRule"
Placement <Plcmnt> contains the following elements (see "ReferredAgent3" on page 5027 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Referred <Rfrd> [1..1] CodeSet 5027
   ReferredPlacementAgent <RfrdPlcmntAgt> [0..1] ± 5027
Constraints
• ReferredPlacementAgentRule
ReferredPlacementAgent may only be present if Referred is REFR (Referred).
3.4.9 NewIssueAllocation <NewIsseAllcn>
Presence: [0..1]
Definition: Confirmation of eligibility conditions applicable when there is an allocation of new issues for
hedge fund account opening.
Approved by the Securities SEG on 27 January 2026 acmt.002.001.08 AccountDetailsConfirmationV08
Investment Funds - Maintenance 2025 - 2026 50 May 2026
```

