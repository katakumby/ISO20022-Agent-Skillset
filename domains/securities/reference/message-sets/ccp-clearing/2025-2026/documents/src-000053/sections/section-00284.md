---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types"]
file_pages: [373]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12 Message Items Types

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 373 to 373.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 373

```text
12 Message Items Types
12.1 MessageComponents
12.1.1 Account
12.1.1.1  SecuritiesAccount18
Definition: Account to or from which a securities entry is made.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 373
   Type <Tp> [1..1] CodeSet 373
   Name <Nm> [0..1] Text 373
12.1.1.1.1  Identification <Id>
Presence: [1..1]
Definition: Unambiguous identification for the account between the account owner and the account
servicer.
Datatype: Max35Text on page 493
12.1.1.1.2  Type <Tp>
Presence: [1..1]
Definition: Specifies if the account is a House, a Client or a Liquidity Provider (Market Maker) account.
Datatype: ClearingAccountType1Code on page 475
CodeName Name Definition
HOUS House Specifies that the account is used to
register trades executed for either the
clearing member or its subsidiaries.
CLIE Client Specifies that the account is used to
register trades executed for the clearing
member's customers.
LIPR LiquidityProvider Specifies that the account is used to
register trades executed for liquidity
providers (also known as market maker)
activities.
12.1.1.1.3  Name <Nm>
Presence: [0..1]
Definition: Description of the account.
Datatype: Max70Text on page 493
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 373
```

