---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["2 acmt.001.001.08 AccountOpeningInstructionV08", "2.4 Message Building Blocks", "2.4.7 Intermediaries <Intrmies>"]
file_pages: [30]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.001.001.08"]
---

# 2.4.7 Intermediaries <Intrmies>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 30 to 30.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 30

```text
AccountParties <AcctPties> contains the following elements (see "AccountParties17" on page 4924 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PrincipalAccountParty <PrncplAcctPty> [1..1]  4925
{Or     PrimaryOwner <PmryOwnr> [1..1] ± 4925
Or     Trustee <Trstee> [1..5] ± 4927
Or     Nominee <Nmnee> [1..1] ± 4929
Or}     JointOwner <JntOwnr> [1..5] ± 4931
   SecondaryOwner <ScndryOwnr> [0..*] ± 4933
   Beneficiary <Bnfcry> [0..*] ± 4935
   PowerOfAttorney <PwrOfAttny> [0..*] ± 4937
   LegalGuardian <LglGuardn> [0..*] ± 4939
   CustodianForMinor <CtdnForMnr> [0..*] ± 4941
   SuccessorOnDeath <SucssrOnDth> [0..*] ± 4943
   Administrator <Admstr> [0..*] ± 4945
   OtherParty <OthrPty> [0..*] ± 4947
   Granter <Grntr> [0..*] ± 4947
   Settlor <Sttlr> [0..*] ± 4949
   SeniorManagingOfficial <SnrMggOffcl> [0..*] ± 4951
   Protector <Prtctr> [0..*] ± 4953
   RegisteredShareholderName <RegdShrhldrNm> [0..1] ± 4955
2.4.7 Intermediaries <Intrmies>
Presence: [0..*]
Definition: Intermediary or other party related to the management of the account.
Approved by the Securities SEG on 27 January 2026 acmt.001.001.08 AccountOpeningInstructionV08
Investment Funds - Maintenance 2025 - 2026 30 May 2026
```

