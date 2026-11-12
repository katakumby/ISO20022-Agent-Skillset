---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.16 Balance30", "82.1.5.16.3 SubAccountDetails <SubAcctDtls>", "82.1.5.16.3.1 AccountOwner <AcctOwnr>"]
file_pages: [2883]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.16.3.1 AccountOwner <AcctOwnr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2883 to 2883.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2883

```text
Constraints
• ActivityAndBalanceForSubAccount1Rule
If the ActivityIndicator is "true" (Yes), then at least one occurrence of BalanceForSubAccount must
be present.
• ActivityAndBalanceForSubAccount2Rule
If the ActivityIndicator is "false" (No), then BalanceForSubAccount must be absent.
• SubSafekeepingReportingRule
Use of consolidated reports on a sub-safekeeping account must be bilaterally agreed between
sender and receiver.
82.1.5.16.3.1  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains one of the following PartyIdentification122Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 2883
Or   NameAndAddress <NmAndAdr> [1..1] ± 2883
Or}   Country <Ctry> [1..1] CodeSet C3 2884
82.1.5.16.3.1.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C2 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 3320
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
82.1.5.16.3.1.2  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2883 August 2026
```

