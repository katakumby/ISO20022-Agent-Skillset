---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["11 seev.039.001.13 CorporateActionCancellationAdviceV13", "11.4 Message Building Blocks", "11.4.3 AccountsDetails <AcctsDtls>"]
file_pages: [710]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.039.001.13"]
---

# 11.4.3 AccountsDetails <AcctsDtls>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 710 to 710.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 710

```text
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
11.4.3 AccountsDetails <AcctsDtls>
Presence: [1..1]
Definition: General information about the safekeeping account and the account owner.
AccountsDetails <AcctsDtls> contains one of the following AccountIdentification73Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ForAllAccounts <ForAllAccts> [1..1] ± 710
Or}   AccountsList <AcctsList> [1..*]  C10,
C11,
C12,
C13
711
     SafekeepingAccount <SfkpgAcct> [0..1] Text 711
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 712
     AccountOwner <AcctOwnr> [0..1] ± 712
     SafekeepingPlace <SfkpgPlc> [0..1] ± 712
11.4.3.1  ForAllAccounts <ForAllAccts>
Presence: [1..1]
Definition: All safekeeping accounts that own underlying financial instrument.
ForAllAccounts <ForAllAccts> contains the following elements (see "AccountIdentification10" on
page 830 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationCode <IdCd> [1..1] CodeSet 830
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 710 February 2026
```

