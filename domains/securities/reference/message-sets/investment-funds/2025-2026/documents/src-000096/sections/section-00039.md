---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["4 acmt.003.001.08 AccountModificationInstructionV08", "4.4 Message Building Blocks", "4.4.6 ModifiedAccountParties <ModfdAcctPties>"]
file_pages: [69]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.003.001.08"]
---

# 4.4.6 ModifiedAccountParties <ModfdAcctPties>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 69 to 69.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 69

```text
4.4.6 ModifiedAccountParties <ModfdAcctPties>
Presence: [0..*]
Definition: Information related to an account party to be inserted, updated or deleted.
Impacted by: C5 "AddressRule"
ModifiedAccountParties <ModfdAcctPties> contains the following elements (see "AccountParties18"
on page 4967 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4969
   PrincipalAccountParty <PrncplAcctPty> [0..1]  4969
{Or     PrimaryOwner <PmryOwnr> [1..1] ± 4969
Or     Trustee <Trstee> [1..5] ± 4971
Or     Nominee <Nmnee> [1..1] ± 4973
Or}     JointOwner <JntOwnr> [1..5] ± 4975
   SecondaryOwner <ScndryOwnr> [0..*] ± 4977
   Beneficiary <Bnfcry> [0..*] ± 4979
   PowerOfAttorney <PwrOfAttny> [0..*] ± 4981
   LegalGuardian <LglGuardn> [0..*] ± 4983
   CustodianForMinor <CtdnForMnr> [0..*] ± 4985
   SuccessorOnDeath <SucssrOnDth> [0..*] ± 4987
   Administrator <Admstr> [0..*] ± 4989
   OtherParty <OthrPty> [0..*] ± 4991
   Granter <Grntr> [0..*] ± 4991
   Settlor <Sttlr> [0..*] ± 4994
   SeniorManagingOfficial <SnrMggOffcl> [0..*] ± 4996
   Protector <Prtctr> [0..*] ± 4998
   RegisteredShareholderName <RegdShrhldrNm> [0..1] ± 5000
Constraints
• AddressRule
If ModificationScopeIndication is INSE (InsertNewDataSet), then one of the following must be
present:
PrincipalAccountParty/./Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
CustodianForMinor/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 69 May 2026
```

