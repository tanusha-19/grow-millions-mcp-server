# GrowMillions MCP Tool Catalog

Complete reference of all 10 registered MCP tools, input schemas, and required permissions.

## 1. Business Profile & Context
- **Tool**: `get_business_profile`
- **Description**: Retrieves registered business metadata, brand guidelines, and core domain parameters.
- **Scope**: `business:read`
- **Arguments**: None

## 2. Marketing Strategy (MarkAI)
- **Tool**: `get_marketing_strategy`
- **Description**: Fetches existing marketing strategy frameworks for the tenant.
- **Scope**: `strategy:read`
- **Arguments**: None

## 3. Strategy Generator
- **Tool**: `generate_marketing_strategy`
- **Description**: Generates a tailored marketing plan based on product and campaign parameters.
- **Scope**: `strategy:read`
- **Arguments**:
  - `product_name` (str, required)
  - `target_audience` (str, optional)

## 4. Content Generator
- **Tool**: `generate_content`
- **Description**: Generates social media copy, post text, or ad copy.
- **Scope**: `content:generate`
- **Arguments**:
  - `prompt` (str, required)
  - `platform` (str, optional, default: `"Instagram"`)

## 5. Social Post Drafting
- **Tool**: `create_post_draft`
- **Description**: Creates an unpublished social post draft in Auto Post.
- **Scope**: `social:write`
- **Arguments**:
  - `content` (str, required)
  - `platform` (str, required)

## 6. Social Post Scheduling (High Risk)
- **Tool**: `schedule_post`
- **Description**: Schedules a social post draft for automatic publication.
- **Scope**: `social:publish`
- **Arguments**:
  - `post_id` (str, required)
  - `scheduled_time` (str, required, ISO format)

## 7. Meta Campaign Drafting
- **Tool**: `create_campaign_draft`
- **Description**: Builds an unpublished draft campaign in Meta Ads Manager.
- **Scope**: `ads:write`
- **Arguments**:
  - `campaign_name` (str, required)
  - `daily_budget` (float, required)

## 8. Meta Campaign Publishing (High Risk / Financial)
- **Tool**: `publish_campaign`
- **Description**: Launches and activates a Meta ad campaign (triggers spending).
- **Scope**: `ads:publish`
- **Arguments**:
  - `campaign_id` (str, required)

## 9. Compliance Calendar
- **Tool**: `get_upcoming_compliances`
- **Description**: Retrieves upcoming tax, GST, and legal marketing deadlines.
- **Scope**: `compliance:read`
- **Arguments**: None

## 10. Automation Marketplace
- **Tool**: `search_marketplace`
- **Description**: Searches available automation concepts and integrations.
- **Scope**: `marketplace:read`
- **Arguments**:
  - `query` (str, required)