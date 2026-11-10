---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.18 Intermediary47", "66.1.30.18.3 Account <Acct>", "66.1.30.18.3.1 Identification <Id>"]
file_pages: [4967, 4968]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.18.3.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4967 to 4968.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4967

```text
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Account <Acct> contains the following Account32 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4967
   AccountServicer <AcctSvcr> [1..1] ± 4967
66.1.30.18.3.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
66.1.30.18.3.2  AccountServicer <AcctSvcr>
Presence: [1..1]
Definition: Institution servicing an account and assigning the account identifier to the account owner.
AccountServicer <AcctSvcr> contains one of the following elements (see
"PartyIdentification125Choice" on page 4909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4909
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4909
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4910
66.1.30.19  AccountParties18
Definition: Information about a party's account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4967 May 2026
```

## File page 4968

```text
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
SecondaryOwner/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
Beneficiary/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet)
PowerOfAttorney/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4968 May 2026
```

